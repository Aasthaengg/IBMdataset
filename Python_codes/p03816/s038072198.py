from collections import Counter
n = int(input())
a = list(map(int, input().split()))
cnt = Counter(a)
x = []
for i, v in cnt.items():
    x.append([i, v])
x.sort()
left = 0
right = len(x) - 1
ans = 0
while left < right:
    if x[left][1] == 1:
        left += 1
    elif x[right][1] == 1:
        right -= 1
    else:
        x[left][1] -= 1
        x[right][1] -= 1
        ans += 2
if x[left][1] == 1:
    pass
else:
    if x[left][1] % 2 == 0:
        ans += x[left][1]
    else:
        ans += x[left][1]-1
print(n - ans)
