import sys

def insertionSort(x_list,y):
  for i in range(1, y):
    v = x_list[i]
    j = i - 1
    while j >= 0 and x_list[j] > v:
      x_list[j + 1] = x_list[j]
      j -= 1
    x_list[j+1] = v
    for k in range(0, y):
      print x_list[k],
    print

y = sys.stdin.readline()
y = int(y)

x = sys.stdin.readline()

x_list = x.split(" ")

for i in range(y):
  x_list[i] = int(x_list[i])

for k in range(0, y):
  print x_list[k],
print

insertionSort(x_list, y)