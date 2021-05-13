
N,Y = map(int,input().split())

Y //= 1000

for n1 in range(N+1):
    y = Y-n1
    n = N-n1

    if y%5 != 0:
        continue
    n10 = (y-5*n)//5
    n5 = n-n10

    if n10 < 0 or n5 < 0:
        continue

    if n1+n5*5+n10*10 == Y:
        n5 = n-n10
        break
else:
    n1,n5,n10 = -1,-1,-1

print(n10,n5,n1)