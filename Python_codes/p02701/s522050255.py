a=int(input())
b=[input() for i in range(a)]
b.sort()
c=0
for i in range(a-1):
  if b[i]==b[i+1]:
    c=c+1
print(a-c)