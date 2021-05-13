n=int(input())
s=input()

ans=s[1:].count('E')
pin=ans

for i in range(1,n):
  if s[i-1]=='W':
    pin+=1
  if s[i]=='E':
    pin-=1
  ans=min(ans,pin)
  
print(ans)