order = input()
counter = 0

for i in range(len(order)):
  if order[i] == 'o':
    counter += 1

ans = 700 + 100*counter
print(ans)