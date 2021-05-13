s=list(input())
S=list(set(s))
ans=100
for c in S:
  kari=0
  tmp=0
  for w in s:
    if w==c:
      kari=max(tmp, kari)
      tmp=0
    else:
      tmp+=1
  kari=max(tmp,kari)
  ans=min(ans, kari)
print(ans)