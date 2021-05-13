#ABC131
N,L = map(int,input().split())
f = 0
k = 0
j = []
for i in range(1,N+1):
    f += L+i-1
for i in range(1,N+1):
    k = L+i-1
    n = f-k
    p = abs(f-n)
    j.append(p)
if f >0:
    print(int(f-min(j)))
else:
    print(int(f+min(j)))
