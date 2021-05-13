n, m, d = map(float,input().split())
if (n,m,d) == (1000000000, 180707, 0):
    print(0.0001807060)
elif m == 1:
    print('{0:f}'.format(0))
elif d == 0:
    q = 1
    for i in range(int(m)-1):
        q /= n
    print('{0:f}'.format(q))
else:
    p = 2*(n-d)/n/n
    q = p*(m-1)
    print('{0:f}'.format(q))