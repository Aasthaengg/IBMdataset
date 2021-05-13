n = input()
n_int = int(n)
a = input().split()
y = 0

for i in range(n_int):
  x = int(a[i])
  y += 1/x

print(1/y)