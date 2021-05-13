n = int(input())
T = 0
H = 0
for i in range(n):
  a, b = input().split()
  if a > b:
    T += 3
  elif a == b:
    T += 1
    H += 1
  else:
    H += 3
print(T, H)
