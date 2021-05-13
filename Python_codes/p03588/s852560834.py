n=int(input())
a=[]
b=[]
for i in range(n):
    c,d=map(int,input().split())
    a.append(c)
    b.append(d)
m=max(a)
j=a.index(m)
print(a[j]+b[j])