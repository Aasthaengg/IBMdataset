n = int(input())
a = [0]*n
b = [0]*n

for i in range(n):
    a[i], b[i] = map(int, input().split())

ans = 0
for i in range(n-1, -1, -1):
    if (a[i]+ans) % b[i] != 0:
        ans += b[i] - (a[i]+ans) % b[i]

print(ans)
