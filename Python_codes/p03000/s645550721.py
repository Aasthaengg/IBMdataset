# coding = SJIS
n, x = map(int, input().split())
lis = list(map(int, input().split()))
ans = 0

bou = [0]
for i in range(n):
    bou.append(bou[i] + lis[i])

for i in range(n + 1):
    if bou[i] <= x:
        ans += 1

print(ans)