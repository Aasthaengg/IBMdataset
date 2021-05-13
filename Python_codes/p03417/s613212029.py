n,m = map(int, input().split())

ans = 0
if n == 1:
    if m == 1:
        ans = 1
    elif m == 2:
        ans = 0
    else:
        ans = m - 2

if n == 2:
    ans = 0

if n > 2:
    if m == 1:
        ans = n-2
    elif m == 2:
        ans = 0
    else:
        ans = (n-2)*(m-2)
    



print(ans)
