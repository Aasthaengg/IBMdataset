n = int(input())

li = []

for i in range(0,(n//2)*2):
  if i+1 < n-i:
    li.append([i+1,n-i-n%2])
  else:
    break
if n%2 == 1:
  li.append([n])
if len(li) > 2:
  li.append(li[0])

count = 0
for i in range(1,len(li)):
  for j in li[i-1]:
    for k in li[i]:
      count += 1
print(count)
for i in range(1,len(li)):
  for j in li[i-1]:
    for k in li[i]:
      print(j,k)