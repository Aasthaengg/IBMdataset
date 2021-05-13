a = [int(input()) for i in range(4)]
count = 0

for i in range(a[0]+1) :
  for j in range(a[1]+1) :
    for k in range(a[2]+1) :
      sum = 500*i + 100*j + 50*k
      if sum == a[3] :
        count += 1
print(count)
