n, k = map(int, input().split())
cnt = 0
ans = 0
a = 0
b = 0
for i in range(1, n+1):
    if i % k == 0:
        a += 1
    elif i % k == k / 2:
        b += 1
ans = a**3 + b**3
print(ans)
