from collections import Counter
n = int(input())
a = list(map(int, input().split()))
c = Counter(a)
bou2 = []
bou4 = []
for k, v in c.items():
    if v > 1:
        bou2.append(k)
    if v > 3:
        bou4.append(k)

bou2.sort(reverse=True)
bou4.sort(reverse=True)
ans = 0
if len(bou2) >= 2:
    ans = bou2[0]*bou2[1]
if len(bou4) != 0:
    ans = max(ans, bou4[0]*bou4[0])
print(ans)


