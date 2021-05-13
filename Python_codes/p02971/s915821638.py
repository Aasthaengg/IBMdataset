n = int(input())
alst = [int(input()) for _ in range(n)]
max_2 = [0, 0]
for a in alst:
  if a > max_2[0]:
    max_2[1] = max_2[0]
    max_2[0] = a
  elif a > max_2[1]:
    max_2[1] = a

for a in alst:
  if a == max_2[0]:
    print(max_2[1])
  else:
    print(max_2[0])