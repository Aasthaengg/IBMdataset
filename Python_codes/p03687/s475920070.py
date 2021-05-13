S = str(input())
ans = 10**18
alp = list(set(S))

for i in alp:
  count = 0
  eff = 0
  for j in S:
    if i != j:
      count += 1
    else:
      eff = max(eff,count)
      count = 0
  eff = max(eff, count)
  ans = min(ans, eff)
  
print(ans)