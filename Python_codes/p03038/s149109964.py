n,m = map(int,input().split())
a = list(map(int,input().split()))
a.sort()
l = []
okikae = []

for i in range(m):
  b,c = map(int,input().split())
  l.append([c,b])
  
l.sort(reverse = True)

for c,b in l:
  for j in range(b):
    if len(okikae) < len(a):
      okikae.append(c)
    else:
      break
  if len(okikae) == len(a):
    break
    
    
for i in range(len(okikae)):
  if okikae[i] > a[i]:
    a[i] = okikae[i]
  else:
    break
    
print(sum(a))