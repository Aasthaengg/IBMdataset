n, a, b = map(int, input().split())
list_x = list(map(int, input().split()))

fatigue = 0
for i, x in enumerate(list_x):
  if i > 0:
    if (x - list_x[i - 1]) * a < b:
      fatigue += a * (x - list_x[i - 1])
    else:
      fatigue += b
print(fatigue)