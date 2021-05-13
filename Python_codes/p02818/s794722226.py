A,B,K = map(int,input().split())
if A >= K:
  ans = [A-K,B]
elif A+B >= K:
  ans = [0,A+B-K]
else:
  ans = [0,0]
print(*ans)