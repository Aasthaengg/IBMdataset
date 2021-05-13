n = int(input())
A = list(map(int,input().split()))

col = [0 for _ in range(9)]
for a in A:
  if a >= 3200:
    col[8] += 1
    continue
  col[a//400] = 1
  
ans_min = sum(col[:-1])
if ans_min == 0 and col[-1] != 0:
  ans_min = 1
print(ans_min, sum(col))

