x, n = map(int, input().split())
if n > 0:
    l = list(map(int, input().split()))
    ans = 0
    for i in range(n):
        if not (x - i) in l:
            ans = x - i
            break
        elif not x + i in l:
            ans = x + i
            break
    print(ans)
else:
    print(x)