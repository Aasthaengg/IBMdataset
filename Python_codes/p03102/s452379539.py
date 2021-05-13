N, M, C = map(int, input().split())
B = list(map(int, input().split()))
solved = 0
for _ in range(N):
  evalue = C
  for A_i, B_i in zip(map(int, input().split()), B):
    evalue += A_i * B_i
  solved += 1 if evalue > 0 else 0
print(solved)