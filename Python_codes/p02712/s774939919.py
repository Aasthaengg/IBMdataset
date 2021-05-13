N = int(input())

i = 1
sum = 0
while (i <= N):
  if(i % 3 != 0 and i % 5 != 0):
    sum = sum + i
  i += 1

print(sum)