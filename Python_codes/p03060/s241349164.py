# coding = SJIS
n = int(input())
valu = list(map(int, input().split()))
cost = list(map(int, input().split()))
ans = 0
for i in range(n):
    if cost[i] < valu[i]:
        ans += valu[i] - cost[i]
    else:
        ans += 0
print(ans)