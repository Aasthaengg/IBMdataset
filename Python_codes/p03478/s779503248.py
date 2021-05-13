n,x,y=map(int,input().split())
c=0
for i in range(1,n+1):
    s=sum(map(int,str(i)))
    if(s>=x and s<=y):
        c+=i
print(c)
