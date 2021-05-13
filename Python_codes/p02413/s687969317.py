import sys
from functools import reduce

(row, column) = sys.stdin.readline().rstrip('\r\n').split(' ')
row = int(row)
column = int(column)

a = []

for ii in range(row):
  a.append([int(x) for x in input().rstrip('\r\n').split(' ')])

for ii in range(len(a)):
  for aa in a[ii]:
    print(str(aa) + ' ', end='')
  print(reduce(lambda sum, x: sum + x, a[ii]))

total = 0
for ii in range(column):
  sum = 0
  for jj in range(row):
    sum += a[jj][ii]
    total += a[jj][ii]
  print(str(sum) + ' ', end='')
print(total)

