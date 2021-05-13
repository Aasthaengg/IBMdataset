S = input()
N = len(S)
a = int(S[:2])
ans = 753
for i in range(2, N):
  a = 10 * a + int(S[i])
  a %= 1000
  ans = min( ans, abs(753-a) )
print(ans)