n=int(input())
e=0
o=0
for i in range(1,n+1):
  if i%2==0:
    e+=1
  else:
    o+=1
print(e*o)