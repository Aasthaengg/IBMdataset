
n,m = map(int, input().split())
ans = n*m
n,m = min(n,m), max(n,m)

if n == 1:
    if m == 1:
        print(1)
    else:
        print(m-2)
    exit()

tmp = n + m - 2
print(ans - tmp * 2)
