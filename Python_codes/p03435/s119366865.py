from itertools import permutations

C = [list(map(int, input().split())) for _ in range(3)]
A = [0, 1, 2]

ans = []

for x in permutations(A, 3):
  temp = 0
  for j in range(3):
    temp += C[j][x[j]]
  ans.append(temp)
    
if len(set(ans)) == 1:
  print("Yes")
else:
  print("No")