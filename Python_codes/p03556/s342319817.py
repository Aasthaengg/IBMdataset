n = int(input())
l = []

for i in range(1,100000):
  l.append(i**2)

for i in range(len(l)):
  if l[i] > n:
    print(l[i-1])
    exit()