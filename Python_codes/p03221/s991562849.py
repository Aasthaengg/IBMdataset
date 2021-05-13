import bisect
def zaatu(a):
    b=list(set(a))
    for i in range(len(a)):
        a[i]=bisect.bisect_left(b,a[i])
    return a
n,m=map(int,input().split())
a=[[] for _ in range(n)]
b=[]
for i in range(m):
    p,y=map(int,input().split())
    a[p-1].append([p,y,i])
for i in range(n):
    a[i].sort(key=lambda x:x[1])
for i in range(n):
    for j in range(len(a[i])):
        b.append([a[i][j],j+1])
b.sort(key=lambda x:x[0][2])
for i in b:
    print('0'*(6-len(str(i[0][0])))+str(i[0][0])+'0'*(6-len(str(i[1])))+str(i[1]))