n = int(input())
d = [0]*n

for i in range(n):
  d[i] = int(input())
  
d.sort()

ans = 0

i = 0
while True:
  if i == n-1:
    break
  if d[i] != d[i+1]:
    ans += 1
    i += 1
  else:
    if max(d) == d[i]:
      break
    else:
      i += 1
print(ans+1)