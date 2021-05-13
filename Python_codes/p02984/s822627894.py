N = int(input())
A = list(map(int,input().split()))
ans = [0]*(N)

hugou = 1
for i in range(0,N,1):
    ans[0]+=A[i]*hugou
    hugou = hugou *(-1)

for i in range(1,N,1):
    ans[i]=2*A[i-1]-ans[i-1]

print(" ".join(list(map(str,ans))))
