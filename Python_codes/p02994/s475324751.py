N,L = map(int,input().split())
ans = 0
for i in range(N):
  ans += i+L
if L>0:
  ans -= L
elif N <= abs(L):
  ans -= L+N-1
print(ans)