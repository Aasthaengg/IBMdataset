n = int(input())
counter = 0
for i in range(1,n+1):
  count = 0
  if i % 2 == 1:
    for j in range(1,i+1):
      if i%j == 0:
        count += 1
      if j == i:
        if count == 8:
          counter += 1
print(counter)