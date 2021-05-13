a,b,c = [int(a) for a in input().split()]
for i in range (a-b):
  c=c-1
  if c==0:
    break
print(c)  