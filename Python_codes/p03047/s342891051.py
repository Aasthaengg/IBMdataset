n,r= map(int, input().split())
c=0
for i in range(1,n+1):
    if i+r<=n+1:
        c+=1
    else:
        exit
        
print(c)