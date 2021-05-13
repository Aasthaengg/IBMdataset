import sys

def bubbleSort(x_list, y):
  a = 0
  flag = 1
  while flag:
    flag = 0
    for i in range(1, y):
      j = y - i
      if x_list[j] < x_list[j - 1]:
        x_list[j], x_list[j - 1] = x_list[j - 1], x_list[j]
        flag = 1
        a += 1
  return a

y = sys.stdin.readline()
y = int(y)

x = sys.stdin.readline()
x_list = x.split(" ")

for i in range(y):
  x_list[i] = int(x_list[i])

a = bubbleSort(x_list, y)

for k in range(0, y):
  print x_list[k],
print
print a