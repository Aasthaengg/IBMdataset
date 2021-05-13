n,m = map(int,input().split())
count = 0
s = 2*n
if m-s < 0:
    print(m//2)
else:
    m -= s
    m = (m//2)//2
    print(n+m)
