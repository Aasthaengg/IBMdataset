N = int(input())

f = [0 for i in range(N)]

for x in range(1, int(N**0.5)+1) :
  for y in range(1, int(N**0.5)+1) :
    for z in range(1, int(N**0.5)+1) :
      n = x*x + y*y + z*z + x*y + y*z + z*x
      if n > N :
        break
      else :
        f[n-1] += 1
        
        
        
for i in range(N) :
  print(f[i])
