from collections import Counter

N=int(input())
A=[int(input()) for _ in range(N)]

c = Counter(A)

if len(c)==N:
  print(N)
  exit()
elif len(c)==N-1:
  print(N-2)
  exit()

ans = 0
for k in c.keys():
  if c[k] % 2 == 1:ans += 1
    
print(ans)