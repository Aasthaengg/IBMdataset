a=input()
b=0
for i in range(len(a)):
  if a[i]!=a[len(a)-i-1]:
    b=b+1
print(int(b/2))