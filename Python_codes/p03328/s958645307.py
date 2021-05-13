a, b = map(int, input().split())

for i in range(1000):
  if b-a == i:
    print(i*(i-1)//2 - a)
    break