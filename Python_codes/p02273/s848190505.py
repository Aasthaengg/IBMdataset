def f():
 global d
 p=[]
 for i in range(len(d)-1):
  a,b=d[i],d[i+1]
  s=a+(b-a)/3;u,t=s+(s-a)*(1+3**.5*1j)/2,b-(b-a)/3
  p+=[a,s,u,t]
 d=p+[d[-1]]
d=[0j,100+0j]
for _ in[0]*int(input()):f()
for e in d:print(e.real,e.imag)
