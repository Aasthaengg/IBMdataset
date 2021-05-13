n, m = (int(i) for i in input().split())
xlist=list(int(i) for i in input().split())
ylist=list(int(i) for i in input().split())

#x=xlist[-1]-xlist[0]
#y=ylist[-1]-ylist[0]

tate=0
yoko=0

for i in range(n-1):
    now=xlist[i+1]-xlist[i]
    now*=(i+1)*(n-i-1)
    tate+=now
    tate%=(10**9+7)


for j in range(m-1):
    now=ylist[j+1]-ylist[j]
    now*=(j+1)*(m-j-1)
    yoko+=now
    yoko%=(10**9+7)

#print(tate, yoko)

print((tate*yoko)%(10**9+7))