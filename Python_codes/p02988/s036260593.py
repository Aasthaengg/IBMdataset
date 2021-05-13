n = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(n-2):
    a = p[i:i+3]
    x = a[1]
    a.sort()
    if a[1] == x:
        ans += 1
print(ans)