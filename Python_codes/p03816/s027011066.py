from collections import Counter
N = int(input())
A = list(map(int, input().split()))

c = Counter(A)

ans = 0
memoflg = False

for k,v in c.most_common():
  #print(k,v)
  while v > 1:
    if v >= 3:
      v -= 2
      ans += 1
    elif v == 2:
      if memoflg:
        memoflg = False
        ans += 1
      else:
        memoflg = True
      v -= 1

if memoflg:
  ans += 1
  
print(N - ans * 2)