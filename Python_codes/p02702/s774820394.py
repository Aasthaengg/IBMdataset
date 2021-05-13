s=list(map(int,list(input())[::-1]))
n=len(s)
cnt=[0]*2019
cnt[0]+=1
c=0
for i in range(n):
  c+=s[i]*pow(10,i,2019)%2019
  cnt[c%2019]+=1
ans=0
for i in cnt:
  if i<=1:
    pass
  else:
    ans+=i*(i-1)//2
print(ans)