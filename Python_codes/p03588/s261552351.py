n=int(input())
ab=[list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    ab[i][1]*=-1
ab.sort()

ans=0

for i in range(n-1):
    ans+=min(ab[i+1][0]-ab[i][0],ab[i+1][1]-ab[i][1])
print(ans+ab[0][0]-ab[-1][1])
