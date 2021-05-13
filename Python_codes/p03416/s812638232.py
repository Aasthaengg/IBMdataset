A, B = map(int, input().split())
S = list(map(str, range(A, B+1)))
ans = 0
for i in range(B-A+1):
  if S[i][0] == S[i][4] and S[i][1] == S[i][3]:
    ans += 1
print(ans)
