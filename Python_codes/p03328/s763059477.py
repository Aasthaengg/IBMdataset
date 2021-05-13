a, b = map(int, input().split())
h = 0
d = b - a 

for i in range(1, 1000):
  h += i
  if i == d:
    print(h - b)
    exit()
