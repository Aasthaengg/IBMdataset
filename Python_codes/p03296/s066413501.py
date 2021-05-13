from numpy import random
n = int(input())
a = list(map(int, input().split()))
b = 0
for i in range (len(a) - 1) :
  if a[i] == a[i + 1]:
    b += 1
    a[i + 1] = random.randint(10000)
print(b)
