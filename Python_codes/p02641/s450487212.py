x,n=map(int,input().split())
p=list(map(int,input().split()))
if(n==0):
    print(x)
    exit()
ans=1000
c=1000
for i in range(-1,102):
    b=1
    for j in range(n):
        if(p[j]==i):
            b=0
    if(b==0):
        continue
    else:
        a=abs(x-i)
        if(ans==a):
            if(c>i):
                c=i
        elif(a<ans):
            ans=a
            c=i
print(c)