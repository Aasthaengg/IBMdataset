n=int(input())
l=[]
while n>0:
    s,y=map(str,input().split())
    if y=='JPY':
        k=int(s)
        l.append(k)
        n-=1
    else:
        j=float(s)*380000
        l.append(j)
        n-=1
print(sum(l))