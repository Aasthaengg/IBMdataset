N=int(input())
retu=[0]*(N+1)
for i in range(N):
    p=int(input())
    retu[p]=retu[p-1]+1
print(N-max(retu))