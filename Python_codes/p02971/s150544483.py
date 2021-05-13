n=int(input())
l=[]
for i in range(n):
    l.append(int(input()))
d=sorted(l)
x=d[-2]
m=max(l)
for i in range(n):
    if(l[i]==m):
        l[i]=x
    else:
        l[i]=m
for i in l:
    print(i)
