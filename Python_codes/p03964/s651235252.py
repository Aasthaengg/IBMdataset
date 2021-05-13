N = int(input())
A, B = map(int, input().split())

for _ in range(N-1):
  T, S = map(int, input().split())
  x = max((A+T-1)//T, (B+S-1)//S)
  A = x*T
  B = x*S

print(A+B)
