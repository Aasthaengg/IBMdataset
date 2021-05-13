s=input()
n=len(s)
cnts=[0]*2019

cnts[0]=1
now=0
for i in range(n-1,-1,-1):
  now+=int(s[i])*pow(10,n-1-i,2019)
  now%=2019
  #print(now)
  cnts[now]+=1

ans=0
for cnt in cnts:
  ans+=cnt*(cnt-1)//2
  
print(ans)
