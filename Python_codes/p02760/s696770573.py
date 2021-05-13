A = [list(map(int, input().split())) for i in range(3)]
N = int(input())
b = [int(input()) for k in range(N)]
hole = [[0,0,0] for i in range(3)]
ans = "No"

for i in range(3):
  for j in range(3):
    for k in range(N):
      if A[i][j] == b[k]:
        hole[i][j] = 1
  flag_hol = 1
  for j in range(3):
    flag_hol *= hole[i][j]
  if flag_hol == 1:
  	ans = "Yes"

flag_diag1 = 1
flag_diag2 = 1
for j in range(3):
  flag_vert = 1
  for i in range(3):
    flag_vert *= hole[i][j]
  if flag_vert ==1:
    ans = "Yes"
  flag_diag1 *= hole[j][j]
  flag_diag2 *= hole[j][2-j]
if (flag_diag1 == 1) or (flag_diag2 == 1):
  ans = "Yes"
  
print(ans)
