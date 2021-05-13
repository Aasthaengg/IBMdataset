A,B,C = [int(i) for i in input().split()]
M = max(A,B,C)
S = A + B + C
ans = 0
if S%2 != M%2:
  ans += 2
ans += int((3*M - S) / 2)
print(ans)