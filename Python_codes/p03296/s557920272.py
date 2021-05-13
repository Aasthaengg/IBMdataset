n = int(input())
a = [int(_) for _ in input().split()]

ans = 0
col = 10001
for i in range(0, n-1):
    if a[i] == a[i+1]:
       ans += 1
       a[i+1] = col
       col += 1

print(ans)
