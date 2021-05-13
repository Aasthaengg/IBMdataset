n, h, w = (int(i) for i in input().split())
e = [[int(i) for i in input().split()] for i in range(n)] 
count = 0
for i in e:
  if i[0] >=h and i[1]>=w:
    count = count+1
print(count)