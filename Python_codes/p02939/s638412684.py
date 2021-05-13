s=input()
n=len(s)
d=[s[0]]
t=0
res=''
for i in range(1,n):
  res+=s[i]
  if res==d[t]:
    continue
  else:
    d.append(res)
    res=''
    t+=1
print(len(d))