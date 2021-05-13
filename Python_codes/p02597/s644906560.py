N = int(input())
c = input()

rw = [0, 0]
for i in range(N):
  if c[i] == 'R':
    rw[0] += 1
  else:
    rw[1] += 1
    
ans = N
left_rw = [0, 0]
right_rw = rw[:]
for i in range(N+1):
  if i == 0:
    pass
  else:
    if c[i-1] == 'R':
      left_rw[0] += 1
      right_rw[0] -= 1
    else:
      left_rw[1] += 1
      right_rw[1] -= 1
      
  ans = min(max(left_rw[1], right_rw[0]), ans)
  
print(ans)