n = int(input())
c = list(input())

count = 0
r = c.count('R')

for i in range(r):
  if c[i] == 'W':
    count += 1
print(count)