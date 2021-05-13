a,b,k = map(int, input().split())

for i in range(a,a+k):
  if i > b:
    break
  print(i)
for i in range(max(b-k+1,a+k),b+1):
  print(i)