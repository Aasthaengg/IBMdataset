x = list(map(int, input().split()))
counter = 0
for i in x:
  counter += 1
  if i == 0:
    print(counter)