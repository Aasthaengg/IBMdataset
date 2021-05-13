k = 0
m = 0
d = int(input())
p = [0]*d
for i in range(d):
  p[i] = int(input())
  if i == 0:
    if p[0] != 0:
      print(-1)
      m = 1
      break
  else:
    if p[i]  <= p[i-1]:
      k += p[i]
    elif p[i] <= 1 + p[i-1]:
      k += 1
    else:
      print(-1)
      m = 1
      break
 
if m != 1:
  print(k)