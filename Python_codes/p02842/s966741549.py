n = int(input())
c=0
for i in range(50000):
  if int(i * 1.08) == n:
    print(i)
    c = 1
    break
if c == 0:
  print(":(")