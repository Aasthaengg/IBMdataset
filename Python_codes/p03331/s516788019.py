n = int(input())
ans = 114514
for i in range(1, n):
    a = list(map(int, list(str(i))))
    b = list(map(int, list(str(n - i))))
    c = sum(a) + sum(b)
    ans = min(ans, c)
print(ans)