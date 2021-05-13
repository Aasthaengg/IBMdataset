from sys import stdin
n = int(stdin.readline().rstrip())
li = list(map(int,stdin.readline().rstrip().split()))
li.sort(reverse=True)
plus = []
minus = []
lin = []
for i in li:
    if i < 0:
        minus.append(i)
    else:
        plus.append(i)
if not plus:
    x = minus[0]
    for i in range(1,n):
        y = minus[i]
        lin.append([x,y])
        x -= y
    print(x)
    for i in lin:
        print(*i)
elif not minus:
    x = plus[-1]
    for i in range(1,n-1):
        y = plus[i]
        lin.append([x,y])
        x -= y
    lin.append([plus[0],x])
    print(plus[0]-x)
    for i in lin:
        print(*i)
else:
    x = minus[-1]
    y = plus[0]
    for i in range(len(minus)-1):
        lin.append([y,minus[i]])
        y -= minus[i]
    for i in range(1,len(plus)):
        lin.append([x,plus[i]])
        x -= plus[i]
    lin.append([y,x])
    print(y-x)
    for i in lin:
        print(*i)