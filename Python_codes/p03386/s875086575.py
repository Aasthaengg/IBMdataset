a,b,k=map(int,input().split())
b+=1
for i in range(a,min(a+k,b)):
  print(i)
for i in range(max(b-k,a+k),b):
  print(i)