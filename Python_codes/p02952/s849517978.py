t = 0
for i in range(1, int(input()) + 1):
  if len(str(i)) % 2 == 1:
    t += 1
print(t)