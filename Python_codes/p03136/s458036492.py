n = int(input())
list = [int(i) for i in input().split()]

max = max(list)
sum = sum(list)

if sum > 2*max:
  print("Yes")
else:
  print("No")