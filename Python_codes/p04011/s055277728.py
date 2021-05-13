n = int(input())
k = int(input())
x = int(input())
y = int(input())

f_normal = x * n
f_addition = x * k  + y * (n - k)

if n <= k:
  print(f_normal)
else:
  print(f_addition)
