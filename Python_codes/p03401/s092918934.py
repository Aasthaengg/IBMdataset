n=int(input())
a=[0]+list(map(int,input().split()))+[0]

#print(a)
s=0
for i in range(n+1):
   s+=abs(a[i+1]-a[i])
   
for i in range(1,n+1):
    si=s+abs(a[i+1]-a[i-1])-abs(a[i+1]-a[i])-abs(a[i]-a[i-1])
    print(si)
