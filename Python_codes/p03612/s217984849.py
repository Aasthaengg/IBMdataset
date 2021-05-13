n = int(input())
l = list(map(int,input().split()))
count = 0
if l[0] == 1:
  l[1] = l[0]
  count += 1
for i in range(1,n):
  if l[i] == i+1:
    if i != n-1:
      if l[i+1] == i+2:
        l[i],l[i+1] = l[i+1],l[i]
        i+=1
    else:
      l[i] = l[i-1]
    count += 1
print(count)