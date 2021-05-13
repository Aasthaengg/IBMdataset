n,m = map(int,(input().split()))
a = []
b=[]
c=[]
for i in range(n):
    k = [int(i) for i in input().split()]
    a.append(k)
for i in range(m):
    x = int(input())
    b.append(x)


for j in range(len(a)):
    c.append(0)
    for k in range(len(a[j])):
        c[j] += a[j][k]*b[k]


for j in c:
    print (j)