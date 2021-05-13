N = int(input())
A = list(map(int,input().split()))

r_s=list(range(0,2801,400))
r_s[0]=1
r_s.append(3200)

r_e=list(range(399,3200,400))
r_e.append(4800)

def check_color(check):
    N=9
    for i in range(N):
        if r_s[i] <= check and r_e[i] >= check:
            return i
        
checklist=[]
checklist_8=[]
for a in A:
#     print( '======')
#     print(a)
    a=check_color(a)
#     print(a)
    if a != 8:
        checklist.append(a)
    else:
        checklist_8.append(a)

max_= len(set(checklist))+len(checklist_8)
min_= len(set(checklist))
        
max_ = max_
min_ = max(1,min_)

print(min_,max_)