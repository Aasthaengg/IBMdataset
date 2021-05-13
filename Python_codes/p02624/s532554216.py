n = int(input())

s = sum(range(1, n + 1))

for i in range(2, n+1):
  t = n // i
  # 1 + 2 + 3 + ... + t
  s += i * (1 + t) * t // 2
#  for j in range(1, n // i + 1):
#    s += i * j

print(s)