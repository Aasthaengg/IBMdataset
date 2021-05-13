N = int(input())
ans = 10**9+7
for i in range(1,N):
  A = i
  B = N-i
  ans = min(ans, sum(list(map(int,str(A))))+sum(list(map(int,str(B)))))
print(ans)