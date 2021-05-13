N = int(input())

masu = [int(i) for i in input().split(' ')]

count = 0
for i in range(len(masu)):
  if (i+1)%2 == 1 and masu[i]%2 == 1:
    count += 1
    
print(count)