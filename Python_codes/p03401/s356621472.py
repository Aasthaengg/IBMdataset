N = int(input())
A = [0]+list(map(int,input().split()))+[0]#size N+2

ans = 0
for i in range(N+1):#当初の計画
    ans+=abs(A[i+1]-A[i])

for i in range(1,N+1,1):#やめること
    sabun= -abs(A[i]-A[i-1])-abs(A[i+1]-A[i])
    sabun += abs(A[i+1]-A[i-1])
    print(ans+sabun)
