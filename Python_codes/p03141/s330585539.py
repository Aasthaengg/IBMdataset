N = int(input())
AB = [0 for _ in range(N)]
SB = 0
for i in range(N):
  A, B = map(int, input().split())
  SB += B
  AB[i] = A + B
AB.sort(reverse=True)
SAB = 0
for i in range(N):
  if i % 2 == 0:
    SAB += AB[i]
print(SAB-SB)