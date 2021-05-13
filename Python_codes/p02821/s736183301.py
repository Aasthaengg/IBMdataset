from scipy.signal import*
n,m,*a=map(int,open(0).read().split())
b=[0]*2**17
for i in a:b[i]+=1
i=2**18-1
c=0
for a in(fftconvolve(b,b)+.5).astype(int)[::-1]:
  i-=1
  if a:
    t=min(m,a)
    c+=i*t
    m-=t
    if not m:break
print(c)