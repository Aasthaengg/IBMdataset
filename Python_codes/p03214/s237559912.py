n = int(input())
a = list(map(int, input().split()))

ave = sum(a)
for i in range(n):
    a[i] = a[i] * n

diff = float("inf")
for i in range(n):
    if abs(a[i] - ave) < diff:
        ans = i
        diff = abs(a[i] - ave)
print(ans)