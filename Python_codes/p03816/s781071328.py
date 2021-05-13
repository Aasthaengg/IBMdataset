N = int(input())
A = list(map(int, input().split()))
B = [0 for i in range(100000)]
cnt = 0
for a in A:
  if B[a-1] == 0:
    B[a-1] = 1
  else:
    cnt += 1
if cnt % 2 == 0:
  print(sum(B))
else:
  print(sum(B)-1)