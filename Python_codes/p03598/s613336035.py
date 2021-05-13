N = int(input())
K = int(input())
MM = input().split()
total = 0
for i in MM:
  x = int(i)
  y = K - int(i)
  if x <= y:
    total += x*2
  else:
    total += y*2
print(total)