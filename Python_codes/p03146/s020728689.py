def f(n):
    if n % 2== 0:
        return n // 2
    else:
        return 3 * n + 1

s = int(input())
ans = 2
if s == 1 or s == 2:
    print(4)
    exit()
while(s > 1):
    s = f(s)
    ans += 1
print(ans)
