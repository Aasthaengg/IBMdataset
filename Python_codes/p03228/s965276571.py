a,b,k = map(int,input().split())
for i in range(k):
  if i % 2 ==0:
    b+= int(a/2)
    a = int(a/2)
  else:
    a += int(b/2)
    b = int(b/2)
print(a,b)