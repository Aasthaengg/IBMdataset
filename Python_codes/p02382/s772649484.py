n=int(input())
x=list(map(float,input().split(' ')))
y=list(map(float,input().split(' ')))

l=[]
for i in range(n):
  if x[i]-y[i]>0:
    l.append(x[i]-y[i])
  else:
    l.append(y[i]-x[i])

D1=0
D2=0
D3=0
Dinf=max(l)

for i in range(n):
  D1+=l[i]
  D2+=l[i]**2
  D3+=l[i]**3
  
D2=D2**(1/2)
D3=D3**(1/3)

print(D1)
print(D2)
print(D3)
print(Dinf)

