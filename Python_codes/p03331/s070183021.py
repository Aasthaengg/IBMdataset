N = int(input())
ans = float('inf')
for i in range(N//2):
  A = i+1
  B = N-A
  ans = min(ans, sum(list(map(int,str(A)))) + sum(list(map(int,str(B))) ))

print(ans)