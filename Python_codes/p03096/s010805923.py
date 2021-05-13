mod=7+10**9
n=int(input())
c=['$']+[int(input()) for _ in [0]*n]
data=[1]+[0]*n
s={}

for i in range(1,n+1):
  if c[i] in s.keys():
    if c[i]!=c[i-1]:
      s[c[i]]+=data[i-1]
      s[c[i]]%=mod
  else:
    s[c[i]]=data[i-1]
  data[i]=s[c[i]]%mod
        
print(data[n])
