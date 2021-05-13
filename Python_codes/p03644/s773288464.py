n=int(input())
m=0
p=1
for i in range(1,n+1):
    if(i%2==0):
        x=i
        c=0
        while(x%2==0):
            c+=1
            x//=2
        if(c>m):
            m=c
            p=i
print(p)
