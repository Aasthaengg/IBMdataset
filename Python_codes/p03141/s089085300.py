n = int(input())
x = [0]*n
for i in range(n):
    a,b = map(int,input().split())
    x[i] = [a,b,a+b]
x.sort(key= lambda val : val[2],reverse=True)

c1 = 0
c2 = 0
for i,[X,Y,Z] in enumerate(x):
    if i%2 == 0:
        c1 += X
    else:
        c2 += Y
print(c1-c2)