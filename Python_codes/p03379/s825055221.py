import copy

n = int(input())
x = list(map(int, input().split()))
num = 0

y = copy.copy(x)
x.sort()
num1 = x[n//2-1]
num2 = x[n//2]

for i in y:
  if i <= num1:
    print(num2)
  else:
    print(num1)