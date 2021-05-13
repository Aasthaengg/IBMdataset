N = int(input())
count_1 = 0
for i in range(1,N+1,2):
  count_2 = 0
  for j in range(1,i+1,2):
    if i % j == 0:
      count_2 += 1
  if count_2 == 8:
    count_1 += 1
print(count_1)  