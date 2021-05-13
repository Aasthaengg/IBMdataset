import sys
N=input()
c=len(N)
N=int(N)
t=((10**c)-1)//9
for i in range(1,10):
  if t*i>=N:
    print(t*i)
    sys.exit()