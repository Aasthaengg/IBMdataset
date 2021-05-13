from bisect import bisect

s=input()

r_inx=[]
l_inx=[]
for i in range(len(s)):
  if s[i]=='R':
    r_inx.append(i)
  else:
    l_inx.append(i)

ans=[0 for i in range(len(s))]

for r in r_inx:
  inx=bisect(l_inx,r)
  dist=l_inx[inx]-r
  if dist%2==0:
    ans[l_inx[inx]]+=1
  else:
    ans[l_inx[inx]-1]+=1

for l in l_inx:
  inx=bisect(r_inx,l)
  inx-=1
  dist=l-r_inx[inx]
  if dist%2==0:
    ans[r_inx[inx]]+=1
  else:
    ans[r_inx[inx]+1]+=1

print(*ans)