n,k,s=open(0).read().split()
n,k=int(n),int(k)
d=0
for i in range(1,n):
  if not s[i]==s[i-1]:
    d+=1
print(n-1-max(d-2*k,0))