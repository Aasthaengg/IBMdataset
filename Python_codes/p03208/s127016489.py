n,k = map(int,input().split())
li = [int(input()) for _ in range(n)]
li.sort()
ans = 10**10
for i in range(n-k+1):
    ans = min(ans,li[i+k-1]-li[i])
print(ans)