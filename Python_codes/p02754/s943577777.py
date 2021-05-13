n,a,b=map(int,input().split())

ab=a+b
num=n//ab
n-=ab*num

if n>=a:
  ans=a
  
else:
  ans=n
  
print(ans+num*a)