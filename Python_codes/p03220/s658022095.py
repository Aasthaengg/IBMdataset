n = int(input())
t, a = map(int, input().split())
h = list(map(int, input().split()))

val = abs(a - t + h[0] * 0.006)
ans = 1

for i in range(1, n):
    avg = abs(a - t + h[i] * 0.006)
    if avg < val:
        val = avg
        ans = i + 1
print(ans)