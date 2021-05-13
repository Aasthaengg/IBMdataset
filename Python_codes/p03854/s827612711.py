s = input()
A = [[5, "dream"], [7, "dreamer"], [5, "erase"], [6, "eraser"]]
g = 0
while len(s) > 0:
  f = 0
  for i in range(4):
    if len(s) >= A[i][0]:
      if s[-A[i][0]:] == A[i][1]:
        s = s[:-A[i][0]]
        f = 1
        break
  if f == 0:
    print("NO")
    g = 1
    break
if g == 0:
  print("YES")