N = int(input())
K = int(input())
x = list(map(int, input().split()))

res = 0
for y_i, x_i in enumerate(x):
  res += min(x_i*2, (K-x_i)*2)
print(res)