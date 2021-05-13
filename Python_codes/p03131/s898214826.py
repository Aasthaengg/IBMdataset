K,A,B = map(int,input().split())

if B-A < 3:
  print(1+K)
  exit()

ans = 1

N = K - (A-1)
if N >= 2:
  ans += A-1
  ans += (B-A)*(N//2) + N%2
else:
  ans += K
print(ans)