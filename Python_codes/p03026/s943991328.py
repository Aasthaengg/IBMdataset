n=int(input())
a=[[]for i in range(n+1)]
for i in range(n-1):
    b,c=map(int,input().split())
    a[b].append(c)
    a[c].append(b)
b=[1]
c=[1]
l=[0]*(n+1)
l[1]=1
while len(b)>0:
    d=[]
    for i in b:
        for j in a[i]:
            if l[j]==0:
                d.append(j)
                c.append(j)
                l[j]=1
    b=d[:]
c=c[::-1]
e=sorted(list(map(int,input().split())))
b=[0]*n
for i in range(n):
    b[c[i]-1]=e[i]
print(sum(e[:-1]))
print(*b)