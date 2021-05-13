from collections import defaultdict
n=int(input())
a_=list(map(int,input().split()))
a=[]
for i,ai in enumerate(a_):
      a.append([1+i,ai])
a.sort(key=lambda x:x[1],reverse=True)
dp=defaultdict(lambda:0)
dp[(0,1)]=max(a[0][1]*(n-a[0][0]),0)
dp[(1,0)]=max(a[0][1]*(a[0][0]-1),0)
for i in range(2,n+1):#i人目の幼児。a[i-1]
      for x in range(i+1):
            y=i-x
            if x==0:
                  dp[(x,y)]=dp[(x,y-1)]+a[i-1][1]*(n-a[i-1][0]-(y-1))
            elif y==0:
                  dp[(x,y)]=dp[(x-1,y)]+a[i-1][1]*(a[i-1][0]-1-(x-1))
            else:
                  dp[(x,y)]=max(dp[(x-1,y)]+a[i-1][1]*(a[i-1][0]-1-(x-1)),dp[(x,y-1)]+a[i-1][1]*(n-a[i-1][0]-(y-1)))
ans=0
for i in range(n+1):
      ans=max(ans,dp[(i,n-i)])
print(ans)
