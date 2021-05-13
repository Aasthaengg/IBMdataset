n=int(input())
m=0
l=0
for i in range(n):
    a=[]
    x,y=map(str,input().split())
    a.append(x)
    a.append(y)
    b=sorted(a)
    if x==y:
        m+=1
        l+=1
    else:
        if x==b[1]:
            m+=3
        elif y==b[1]:
            l+=3
print(m,l)
