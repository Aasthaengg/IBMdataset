a,b,k=map(int,input().split())
for i in range(k):
  if i % 2 == 0:
    give = a//2
    a = a//2
    b += give
  else:
    give = b//2
    b = b//2
    a += give
print(a,b)