n,k,x,y=[int(input())for i in [0]*4]
ans=0
ans+=min(k,n)*x
n-=min(k,n)
print(ans+y*n)