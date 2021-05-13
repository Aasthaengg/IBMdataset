from collections import Counter

N = int(input())
A = list(map(int,input().split()))

C = Counter(A)

ans = 0
for x,c in C.items():
  t = c
  if c >= x:
    t = min(t,c-x)
  ans += t
  
print(ans)

