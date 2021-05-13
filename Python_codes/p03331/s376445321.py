n = int(input())
N = n//2
ans = float("INF")
for i in range(1,N+1):
  a,b = list(str(i)), list(str(n-i))
  A,B = sum(list(map(int, a))), sum(list(map(int, b)))
  if ans > A+B: ans = A+B
print(ans)