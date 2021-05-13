abc = list([int(i)  for i in input().split()])
k = int(input())

Max = max(abc)
for i in range(0,k):
  Max = Max * 2

Sum = sum(abc) - max(abc) + Max
print(Sum)
  

