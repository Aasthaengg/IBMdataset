n = int(input())
ans = 46
for i in range(1, n):
    tmp = 0
    j = n - i
    while i > 0:
        tmp += i % 10
        i //= 10
    while j > 0:
        tmp += j % 10
        j //= 10
    ans = min(tmp, ans)
print(ans)