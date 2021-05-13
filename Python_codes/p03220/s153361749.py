n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

a -= t
a *= 1000

ans = 0
diff = abs(a + h[0] * 6)

for i in range(1, n):
    if abs(a + h[i] * 6) < diff:
        ans = i
        diff = abs(a + h[i] * 6)

print(ans + 1)