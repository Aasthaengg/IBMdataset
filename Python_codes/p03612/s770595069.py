N = int(input())
values = [ int(v) for v in input().split(" ") ]

left = None
right = None
n = 0

for i in range(N):
  if values[i] == i+1: # NG pattern
    if i == 0:
      values[i], values[i+1] = values[i+1], values[i] # exchange right
    elif i == N-1:
      values[i], values[i-1] = values[i-1], values[i] # exchange left
    elif left == i+1:
      values[i], values[i+1] = values[i+1], values[i] # exchange right
    elif right == i+1:
      values[i], values[i-1] = values[i-1], values[i] # exchange left
    else:
      values[i], values[i+1] = values[i+1], values[i] # exchange right
      
    n += 1
    
#print(values)
print(n)