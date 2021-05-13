n=int(input())
d={}
ans=0
for _ in range(n):
  s = ''.join(sorted(input()))
  if s in d.keys():
    d[s] += 1
    ans += d[s]
  else:
    d.setdefault(s,0)
print(ans)