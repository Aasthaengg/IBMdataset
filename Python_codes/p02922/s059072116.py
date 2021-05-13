A,B = map(int,input().split())
 
for i in range(100):
  if (i*A -(i-1)) >= B:
    break
print(i)