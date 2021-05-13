from collections import Counter
n = int(input())
v = list(map(int, input().split()))
odd = [v[2*i] for i in range(n//2)]
even = [v[2*i+1] for i in range(n//2)]

co = Counter(odd)
ce = Counter(even)
co = co.most_common()
ce = ce.most_common()
if co[0][0] == ce[0][0]:
  if (len(co)>1) and (len(ce)>1):
    ans = min(n//2-co[1][1]+n//2-ce[0][1], n//2-co[0][1]+n//2-ce[1][1])
  elif len(co) > 1:
    ans = n//2 - co[1][1]
  elif len(ce) > 1:
    ans = n//2 - ce[1][1]
  else:
    ans = n//2
else:
  ans = n//2-co[0][1] + n//2-ce[0][1]
print(ans)