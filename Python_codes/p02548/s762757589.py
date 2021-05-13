n = int(input())
a = 0
for i in range(1,n):
  for j in range(i,n,i):
    a+=1
print(a)