n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
b.append(0)
ans = 0
for i in range(n + 1):
    m = min(a[i], b[i - 1])
    a[i] -= m
    b[i - 1] -= m
    ans += m
    m = min(a[i], b[i])
    a[i] -= m
    b[i] -= m
    ans += m
print(ans)