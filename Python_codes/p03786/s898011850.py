n=int(input())
A=list(map(int,input().split()))
A.sort()
ans=1
s=0
for i in range(n):
    if 2*s>=A[i]:
        ans+=1
    else:
        ans=1
    s+=A[i]
print(ans)