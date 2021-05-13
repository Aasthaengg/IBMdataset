N,M = list(map(int,input().split()))

f=[]
for m in range(1,int(M**(1/2))+3):
    if M % m == 0:
        f.extend([m,M//m])
f.sort(reverse=True)

for f_ in f:
    if N <= M/f_:
        ans=f_
        break
print(ans)