c = [list(map(int,input().split())) for _ in range(3)]

a1 = 0
b1 = c[0][0]

a2 = c[1][0]-c[0][0]
a3 = c[2][0]-c[0][0]

b2 = c[0][1]
b3 = c[0][2]

A = [[a1,a1,a1],[a2,a2,a2],[a3,a3,a3]]
B = [[b1,b2,b3],[b1,b2,b3],[b1,b2,b3]]

C = c

ans = "Yes"

for x in range(3):
  for y in range(3):
    if A[x][y] + B[x][y] != C[x][y]:
      ans = "No"
      break
print(ans)