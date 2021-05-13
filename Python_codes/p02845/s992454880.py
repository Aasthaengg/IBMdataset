n=int(input())
A=[int(i) for i in input().split()]
mod=10**9+7

t=[0,0,0]
ans=1

for i in range(n):
    now=A[i]
    cnt=0
    for q in range(3):
        if t[q]==now:
            cnt+=1
    ans=ans*cnt%mod
    for q in range(3):
        if t[q]==now:
            t[q]+=1
            break

print(ans)