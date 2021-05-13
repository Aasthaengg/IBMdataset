A,B,C = map(int,input().split())
ans = 0
if A == B == C:
  if A%2 != 0 or B%2 != 0 or C%2 != 0:
    pass
  else:
    ans = -1
else:
  while A%2 == 0 and B%2 == 0 and C%2 == 0:
    A,B,C = B//2+C//2,A//2+C//2,A//2+B//2
    ans += 1
print(ans)