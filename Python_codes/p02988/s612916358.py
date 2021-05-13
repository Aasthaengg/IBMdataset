N = int(input())
p = list(map(int, input().split()))

ans = 0
for i in range(1, N - 1):
    l = p[i - 1: i + 2]
    a = sorted(l)
    if a[1] == l[1]:
        ans += 1
print(ans)