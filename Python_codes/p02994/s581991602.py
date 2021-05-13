n, l = map(int, input().split())
a = [l] * n
ans = 0
for i in range(1, n):
    a[i] += i
    if abs(a[ans]) > abs(a[i]):
        ans = i
print(sum(a) - a[ans]) 