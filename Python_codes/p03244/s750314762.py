n,*v=map(int,open(0).read().split())
a,b={},{}
for i,j in zip(v[::2],v[1::2]):	
  a[i]=a.get(i,0)+1
  b[j]=b.get(j,0)+1
A=list(a.items())
B=list(b.items())
A.sort(key=lambda x: x[1])
B.sort(key=lambda x: x[1])
c,d=A[-1][1],B[-1][1]
if len(set(v))==1:
    print(n//2)
    exit()
if A[-1][0]==B[-1][0]:
    if c==d:
        c=max(A[-2][1],B[-2][1])
    elif c>d:
        d=B[-2][1]
    else:c=A[-2][1]    
print(n-c-d)