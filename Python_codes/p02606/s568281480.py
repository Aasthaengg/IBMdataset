num = [int(i) for i in input().split()]
n = 0
for i in range(num[0], num[1]+1):
  if i % num[2] == 0:
    n += 1
print(n)