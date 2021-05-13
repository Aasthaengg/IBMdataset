n=int(input())
ab = []
for _ in range(n):
    a, b = (int(x) for x in input().split())
    ab.append([a, b])
ans = 0

for i in range(n-1,-1,-1):
    ans += (ab[i][1]-(ab[i][0]+ans)%ab[i][1])%ab[i][1]
print(ans)