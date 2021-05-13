k=int(input())
t=100
c=0
while k>t:
  t+=t//100
  c+=1
print(c)