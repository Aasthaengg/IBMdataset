n = int(input())
h = list(map(int, input().split()))
ar = []
count = 0
for i in range(n-1):
  
  if h[i] >= h[i+1]:
    count += 1
    ar.append(count)
  else:
    
    count = 0
if ar == []:
  print(0)
else:
  print(max(ar))