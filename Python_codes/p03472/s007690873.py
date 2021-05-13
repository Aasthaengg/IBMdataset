n,h=map(int, input().split())
a_l=[]
b_l=[]
for _ in range(n):
    a,b=map(int, input().split())
    a_l.append(a)
    b_l.append(b)
a_l.sort(reverse=True)
b_l.sort(reverse=True)
a_max=max(a_l)

b_strong=[]
for b_i in b_l:
    if b_i>a_max:
        b_strong.append(b_i)

cnt=0
for b_s in b_strong:
    if h>0:
        h-=b_s
        cnt+=1
    else:
        break

if h>0:
    cnt+=(h-1)//a_max+1

print(cnt)
