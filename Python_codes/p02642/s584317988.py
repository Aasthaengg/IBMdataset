import itertools
N = int(input())
A = list(map(int, input().split()))
count = {}
for a in A:
  if a not in count:
    count[a] = 0
  count[a] += 1

def check(a):
  if count[a] > 1:
    return 0

  if 1 in count:
    if a == 1 and count[1] == 1:
      return 1
    return 0

  #print(a)
  ok = True
  sqr_a = 1 + int(a**0.5)
  for s in itertools.chain([2], range(3, sqr_a, 2)):
    if a % s:
      continue
    c = s
    while c < sqr_a:
      if a % c == 0 and (c in count or (a//c) in count):
        #print(a, c)
        ok = False
        break
      c *= 2
  return ok
  
ans = 0
for a in A:
  ans += check(a)
print(ans)
    
    

