l = []
while True:
  h,w = map(int,input().split())
  if (h,w) == (0,0):
    break
  else:
    l.append([h,w])
for i in l:
  for j in range(i[0]):
    print('#'*i[1])
  print()