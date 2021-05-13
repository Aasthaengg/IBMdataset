K = int(input())
A, B = map(int, input().split())
ans = "NG"
if A % K == 0:
  ans = "OK"
elif B % K == 0:
  ans = "OK"
elif A // K != B // K:
  ans = "OK"
print(ans)