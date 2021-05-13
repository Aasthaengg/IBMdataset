nm=list(map(int,input().split()))
a=[[0 for x in range(nm[1])]for x in range(nm[0])]
b=[0 for x in range(nm[1])]
for x in range(nm[0]):
    code=list(map(int,input().split()))
    for y in range(nm[1]):
        a[x][y]=code[y]
for x in range(nm[1]):
    b[x] = int(input())

for x in range(nm[0]):
    result=0
    for y in range(nm[1]):
        result+=a[x][y]*b[y]
    print(result)