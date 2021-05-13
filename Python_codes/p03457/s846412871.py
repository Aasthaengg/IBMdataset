ans = "Yes"
N = int(input())
t = [0]
x = [0]
y = [0]
for i in range(N):
  tmp = input().split(" ")
  t.append(int(tmp[0]))
  x.append(int(tmp[1]))
  y.append(int(tmp[2]))

for j in range(N):
  dt = t[j+1] - t[j]
  dx = abs(x[j+1] - x[j])
  dy = abs(y[j+1] - y[j])
  if dt >= dx + dy and dt % 2 == (dx + dy) % 2:
    continue
  else:
    ans = "No"
    break

print(ans)