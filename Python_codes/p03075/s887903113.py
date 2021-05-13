import sys
a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())
L=[a,b,c,d,e]
for i in range(4):
  for j in range(i+1,5):
    if abs(L[i]-L[j])>k:
      print(":(")
      sys.exit()
print("Yay!")