n = int(input())
p_t = 0
p_h = 0

for i in range(n):
  t,h = str(input()).split()
  if t > h:
    p_t += 3
  elif t < h:
    p_h += 3
  else:
    p_t += 1
    p_h += 1

print (str(p_t) + " " + str(p_h))
