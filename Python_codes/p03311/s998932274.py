N=int(input())
A=list(map(int, input().split()))
B=[A[i]-i-1 for i in range(N)]
B=sorted(B)

center=B[N//2] if N%2==1 else round((B[(N-1)//2]+B[(N+1)//2])/2)
ans=0
for i in B:
    ans+=abs(i-center)
print(ans)