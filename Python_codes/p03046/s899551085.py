import sys
m,k=map(int,input().split())
if k>=2**m:
    print(-1)
    sys.exit()
if m==1:
    if k==0:
        xor=[0,0,1,1]
        print(' '.join(map(str,xor)))
    else:
        print(-1)
    sys.exit()
idx=0
xor=[0]*(2**(m+1))

for i in range(2**m-1):
    if idx==k:
        idx+=1
    xor[i]=idx
    idx+=1
xor[2**m-1]=k
idx=2**m-1
for i in range(2**m,2**(m+1)-1):
    if idx==k:
        idx-=1
    xor[i]=idx
    idx-=1
xor[-1]=k
print(' '.join(map(str,xor)))