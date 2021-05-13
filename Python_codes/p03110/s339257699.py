bi=380000
n=0
for i in range(int(input())):
  p,s=input().split()
  if s=="JPY":n+=int(p)
  else:n+=bi*float(p)
print(n)