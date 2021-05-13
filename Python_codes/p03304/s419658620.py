n,m,d = map(int,input().split())
if(d==0):
    ans=(m-1)/n
elif(n/d<2):
    ans=2*(m-1)*(n-d)/n
else:
    ans=2*(m-1)*(n-d)/(n*n)
print(ans)
