N = int(input())
A = {}
B = []
for n in range(N):
    a,b = list(map(int,input().split()))
    B.append(b)
    
    if b not in A.keys():
        A[b] = [a]
    else:
        A[b].append(a)

B=list(set(B))
B.sort()

time=0
ans='Yes'
break_flag = False

for b in B:
    if break_flag:
        break
    for a in A[b]:
        time += a 
#         print(b,a,time)
        if b < time:
            ans='No'
            break_flag = True
            break
        
print(ans)