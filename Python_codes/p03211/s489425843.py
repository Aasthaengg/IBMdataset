N=input()
l=753
sa=999999999999
for i in range(len(N)-2):
  k=int(N[i]+N[i+1]+N[i+2])
  #print(k)
  if abs(k-l)<sa: sa=abs(k-l)
print(sa)