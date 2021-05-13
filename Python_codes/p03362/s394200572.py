l=[]
for i in range(6,1382,5):
  f=True
  for j in range(2,int(i**0.5)+1):
    if i%j==0:
      f=False
      break
  if f:
    l.append(i)

print(" ".join(map(str,l[:int(input())])))