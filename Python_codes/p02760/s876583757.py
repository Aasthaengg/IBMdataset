arr = []
b = []
cmp_arr = [[False] * 3 for _ in range(3)]

for i in range(3):
  arr.append(list(map(int,input().split())))

N = int(input())
for i in range(N):
  b.append(int(input()))

for i in range(3):
  for j in range(3):
    for k in range(N):
      if arr[i][j] == b[k]:
        cmp_arr[i][j] = True

for i in range(3):
  if cmp_arr[i][0] and cmp_arr[i][1] and cmp_arr[i][2]:
    print("Yes");exit()
  if cmp_arr[0][i] and cmp_arr[1][i] and cmp_arr[2][i]:
    print("Yes");exit()

if cmp_arr[0][0] and cmp_arr[1][1] and cmp_arr[2][2]:
  print("Yes");exit()
if cmp_arr[0][2] and cmp_arr[1][1] and cmp_arr[2][0]:
  print("Yes");exit()
print("No")