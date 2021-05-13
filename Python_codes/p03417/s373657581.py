n, m = map(int, input().split())
if n < 2:
    n = 3
if m < 2:
    m = 3
ans = (n-2)*(m-2)
if ans < 0:
    ans = 0
print(ans)