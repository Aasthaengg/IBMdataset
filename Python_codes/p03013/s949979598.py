import sys
n,m=map(int,input().split())
a=[]
d=0
for i in range(m):
    a.append(int(input()))
a.append(0)
a.append(0)
a.append(0)
ans=[]
for i in range(m-1):
    if a[i+1]-a[i]==1:
        print(0)
        sys.exit()
ans=[0 for i in range(n+5)]
ans[1]=1
ans[2]=2

if a[0]==1:
    ans[1]=0
    ans[2]=1
    d+=1
if a[0]==2 or a[1]==2:
    ans[2]=0
    d+=1

for i in range(1,n+3):
    if i+2==a[d]:
        ans[i+2]=0
        d+=1
    else:
        ans[i+2]=ans[i+1]%1000000007+ans[i]%1000000007
   
print(ans[n]%1000000007)
    
    
    

        
