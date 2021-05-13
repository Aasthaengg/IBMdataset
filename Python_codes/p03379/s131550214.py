import sys

read = sys.stdin.buffer.read

n,*x = list(map(int, read().split()))
x_sort = sorted(x)

mean_left = x_sort[n//2-1]
mean_right = x_sort[n//2]


for i in range(n):
  if x[i] <= mean_left:
    print(mean_right)
  elif x[i] >= mean_right:
    print(mean_left)