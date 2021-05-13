s=list(input())
t=input()
k=[]
for i in range(len(s)-len(t)+1):
  m=i
  for j in t:
    if s[m]==j or s[m]=='?':
      m+=1
    else:break
  else:
    l=s[:i]+list(t)+s[i+len(t):]
    for i in l:
      if i=='?':
        l[l.index(i)]='a'
    k.append(''.join(l))
if len(k)==0:
  k.append('UNRESTORABLE')
print(min(k))