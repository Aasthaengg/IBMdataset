c = [list(map(int, input().split())) for i in range(3)]
x = c[0][2] - c[0][1]
y = c[0][1] - c[0][0]
ans = 'Yes'
for i in range(1, 3):
  if c[i][2] - c[i][1] != x or c[i][1] - c[i][0] != y:
    ans = "No"
    break

print(ans)
