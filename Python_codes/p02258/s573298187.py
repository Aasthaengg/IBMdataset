n = raw_input()
n = int(n)
minv = raw_input()
minv = int(minv)
maxv = -1000000000
  
for j in range(n-1):
  num = raw_input()
  num = int(num)  
  diff = num - minv
  if maxv < diff:
    maxv = diff
  if num < minv:
    minv = num
  
print maxv