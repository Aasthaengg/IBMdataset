s = input()
t = set(s)
ans = 10**10
for c in t:
  cnt = 0
  x = s
  while len(set(x))!=1:
    ns = ''
    for i in range(len(x)-1):
      if x[i]==c or x[i+1]==c:
        ns += c
      else:
        ns += x[i]
    if ns==x:
      break
    x = ns
    cnt += 1
  else:
    ans = min(cnt,ans)
print(ans)