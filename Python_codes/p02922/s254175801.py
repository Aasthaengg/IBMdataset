a, b = map(int,input().split(" "))

for i in range(20):
  d = (a-1)*i +1
  if d >= b:
    print(i)
    break
