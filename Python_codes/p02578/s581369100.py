N = int(input())
A = list(map(int, input().split()))

step = 0
highest = 0
for a in A:
  if a >= highest:
    highest = a
  else:
    step += highest-a
    
print(step)