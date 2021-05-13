n = int(input())
TA = [list(map(int, input().split())) for _ in range(n)]

T = A = 1
for t, a in TA:
  r = max(A//a, T//t)
  if r*a >= A and r*t >= T:
    A = r*a; T = r*t
  else:
    A = (r+1)*a; T = (r+1)*t

print(T+A)