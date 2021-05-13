n = int(input())

l = [0] * (n+1)

for i in range(n+1):
  if i == 0:
    l[0] = 2
  elif i == 1:
    l[1] = 1
  else:
    l[i] = l[i-2] + l[i-1]
    
print(l[n])