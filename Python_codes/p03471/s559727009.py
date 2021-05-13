import sys
n,y=map(int,input().split())

for ykc in range(0,y+1,10000):
  for ntb in range(0,y-ykc+1,5000):
    ntm=(y-ykc-ntb)
    nntm=ntm//1000
    nntb=ntb//5000
    nykc=ykc//10000
    if ntm%1000==0 and (nntm+nntb+nykc==n):
      print(nykc, nntb, nntm)
      sys.exit()
print('-1 -1 -1')
