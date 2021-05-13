a=int(input())
b=int(input())
c=int(input())
d=int(input())
e=int(input())
k=int(input())

m=min(a,b,c,d,e)
M=max(a,b,c,d,e)

if M-m<=k:
  print("Yay!")
else:
  print(":(")