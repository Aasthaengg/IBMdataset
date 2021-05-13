n = int(input())
s = input()
wh = [0] * n
bl = [0] * n

w , b = 0,0
for i in range(n):
  if s[i] == '.':
    w += 1
  else:
    b += 1
  wh[i] = w
  bl[i] = b
ans = n
wtot = wh[-1]
btot = bl[-1]
for i in range(n):
  x = (wtot - wh[i]) + bl[i]
  # print (bl[i], (wtot - wh[i]))
  ans = min(ans, x)
ans = min(ans, wtot)
print (ans)