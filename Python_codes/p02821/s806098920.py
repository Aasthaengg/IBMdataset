from numpy import*
n,m,*a=int_(open(0).read().split())
b=[0]*2**18
for i in a:b[i]+=1
i=2**18
c=0
for a in int_(fft.irfft(fft.rfft(b)**2)+.5)[::-1]:
  i-=1
  if a:
    t=min(m,a)
    c+=i*t
    m-=t
    if not m:break
print(c)