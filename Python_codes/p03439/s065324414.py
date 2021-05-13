N = int(input())
seat = ['?' for _ in range(N+1)]
left = 0
right = N
for i in range(20):
  if i == 0:
    output = 0
  elif i == 1:
    output = (N-1)//2
  else:
    output = (right + left)//2
  print(output)
    
  s = input()
  if s == 'Vacant':
    exit()
  seat[output] = s
  if i == 0:
    seat[N] = s
  #print(seat)
  if ((right + output) % 2 == 0 and seat[right] != seat[output]) or ((right + output) % 2 == 1 and seat[right] == seat[output]):
    left = output
  else:
    right = output
