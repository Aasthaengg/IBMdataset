N,L=map(int, input().split())

all=0
now=0
for i in range(N):
    all =all +L+(i+1)-1
 
dif=all
for i in range(N):
    if abs(dif) >= abs(L+i):
        dif =L+i
 
print(all-dif)