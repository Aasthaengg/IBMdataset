n=int(input())
ans=0
for i in range(n+1):
  for j in range(n+1):
    if i*4+j*7==n:
      ans=1
print(["No","Yes"][ans])