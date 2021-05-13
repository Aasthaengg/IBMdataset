h = int(input())

power = 0
while True:
  if 2**power <= h < 2**(power+1):
    break
  else:
    power += 1
    
layer = power + 1
ans = int(2**layer) - 1
print(ans)