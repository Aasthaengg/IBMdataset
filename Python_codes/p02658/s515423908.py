N=int(input())
A=list(map(int,input().split()))
A=sorted(A)
ans=1

for i in range(N):
    ans=ans*A[i]
    if ans>10**18:
        print(-1)
        exit()
print(ans)
