L=input()
a=1
b=2
c=10**9+7
for i in range(1,len(L)):
  if L[i]=="0":
    a=a*3%c
  else:
    a=(a*3+b)%c
    b=b*2%c
print((a+b)%c)