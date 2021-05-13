n=int(input())
s={}
for i in range(n):
  tmp=list(input().strip())
  tmp.sort()
  tmp="".join(tmp)
  s[tmp]=s.get(tmp,0)+1
  
ans=0
for key in s.keys():
  v=s[key]
  if v<2:
    continue
  cmb=v*(v-1)
  cmb=cmb//2
  ans+=cmb
print(ans)
