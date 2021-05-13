n,m,d = map(int,input().split())

if d == 0:
    Xk = n/(n**2)
else:
    Xk = 2*(n-d)/(n**2)

L = m-1

print(Xk*L)