from sys import exit

n = int(input())
s = sorted([int(input()) for _ in range(n)])

sum_s = sum(s)

if sum_s % 10 > 0:
  print(sum_s)
  exit()

for v in s:
  if (sum_s - v) % 10 > 0:
    print(sum_s - v)
    exit()

print(0)