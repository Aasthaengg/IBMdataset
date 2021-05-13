N = int(input())
S = sorted([int(input()) for _ in range(N)])
 
m = 0
for s in S:
  if s % 10 != 0 and m == 0:
    m = s
    break
ans = sum(S)
if ans % 10 != 0:
  print(ans)
elif m != 0:
  print(ans-m)
else:
  print(0)