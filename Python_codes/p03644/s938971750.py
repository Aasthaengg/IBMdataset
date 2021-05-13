n=int(input())
c=1
i=1
while n>=2**i:
  c=2**i
  i+=1
print(c)