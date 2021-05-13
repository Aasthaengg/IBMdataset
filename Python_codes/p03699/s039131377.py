N = int(input())
S = [int(input()) for n in range(N)]
A = sum(S)

if A%10!=0:
  ans = A
else:
  T = [s for s in S if s%10!=0]
  if len(T)==0:
    ans = 0
  else:
    ans = A-min(T)

print(ans)