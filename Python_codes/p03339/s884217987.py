n=int(input())
s=input()
e=[int("E"==i) for i in s]
for i in range(1,n):
  e[i]+=e[i-1]

  
ans=[]
for j in range(n):
  left=j-0
  right=n-j-1
  
# leftにWは何個？
# leftのEは、
  if j-1>=0:
    etmp=e[j-1]
  else:
    etmp=0
  leftw=left-etmp
# rightにEは何個？
# rightのEは、
  eee=e[n-1]-e[j]
  ans+=(leftw+eee),
print(min(ans))
