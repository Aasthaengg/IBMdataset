n = int(input())
a = list(map(int, input().split()))
l = [0] * n
r = [0] * n

for i, h in enumerate(a):
    if 0 <= i + h < n:
        l[i + h] += 1
    if 0 <= i - h < n:
        r[i - h] += 1

ans = 0
for i in range(n):
    ans += l[i] * r[i]
print(ans)
