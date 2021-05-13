n, x, t = map(int, input().split())

a = int(n/x)

b = n%x

if(b>0):
    a += 1



print(int(t*a))
