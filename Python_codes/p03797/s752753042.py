n,m = map(int,input().split())
if n > m//2:
    print(m//2)
else:
    tmp = m - 2 * n
    print(n + tmp//4)
