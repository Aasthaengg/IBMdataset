ni = lambda: int(input())
nm = lambda: map(int, input().split())
nl = lambda: list(map(int, input().split()))

n=ni()
s = [_ for _ in input()][::-1]

a = set()
ans=0
ii = set()
for i in range(n-2):
  if s[i] in ii:
    continue
  ii.add(s[i])
  jj = set()
  for j in range(i+1,n-1):
    if s[j] in jj:
      continue
    jj.add(s[j])
    kk = set()
    for k in range(j+1,n):
      if k not in kk:
        ans+=1
        kk.add(s[k])
        a.add(''.join([s[k],s[j],s[i]]))
    
print(len(a))
