s = int(input())
a = s
prev = set()
for i in range(1, 1500000):
  if a in prev:
    print(i)
    exit()
  prev.add(a)
  if a % 2 == 0:
    a //= 2 
  else:
    a = 3 * a + 1