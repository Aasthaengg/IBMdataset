n = int(input())
a = [int(x) for x in input().split()]

suma = sum(a)
x = a[0]
ans = abs(suma - x * 2)

for i in range(1, n - 1):
    x += a[i]
    ans = min(ans, abs(suma - x * 2))
else:
    print(ans)