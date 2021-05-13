n,m = map(int,input().split())
if m >= 2*n:
    m -= 2*n
    print(n+int(m/4))
else:
    print(int(m/2))

