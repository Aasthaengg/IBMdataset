n=int(input())
a,b,c=list(map(int,input().split())),0,[]
for i in range(n):
    if i!=n-1:
        if a[i]==a[i+1]:
            b+=1
        else:
            c.append(b+1)
            b=0
    else:
        c.append(b+1)
        b=0
for i in range(len(c)):
    b+=c[i]//2
print(b)