CONST=10**100
ss=list(input())
res=[0]*len(ss)
lc=0
rc=0
pos=-1
for i,s in enumerate(ss):
  if i < len(ss)-1 and s=='R' and ss[i+1]=='L':
    # last
    lc+=1
    pos=i
    continue
  if (i < len(ss)-1 and s=='L' and ss[i+1]=='R') or i==len(ss)-1:
    # border
    rc+=1
    res[pos] = (lc+1)//2 + rc//2
    res[pos+1] = lc//2 + (rc+1)//2
    lc=0
    rc=0
    continue
  if s=='L':
    rc+=1
  else:
    lc+=1
print(*res)