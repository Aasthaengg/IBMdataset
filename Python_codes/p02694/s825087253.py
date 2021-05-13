x = int(input())
a = 100
for i in range(1, 5000):
  a = (a * 101) // 100
  if a >= x:
    print(i)
    exit()