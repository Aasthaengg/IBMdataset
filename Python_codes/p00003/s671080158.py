n=int(input())
a=[]
c=[]
for i in range(n):
    a.append([])
    for j in range(3):
        a[i].append([])
for i in range(n):
    #for j in range(3):
    a[i][0], a[i][1], a[i][2]=map(int, input().split())
    a[i].sort()
    if(((a[i][0]*a[i][0])+(a[i][1]*a[i][1]))==(a[i][2]*a[i][2])):
        k="YES"
        c.append(k)
    else:
        k="NO"
        c.append(k)
for i in range(n):
    print(c[i])