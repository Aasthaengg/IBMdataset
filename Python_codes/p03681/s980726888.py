MOD = 10**9+7

N,M = map(int,input().split())

if abs(N-M)>1:
    print(0)
    exit()

#N=Mなら最後に2をかける
dog = 1
monkey = 1
for i in range(1,N+1):
    dog = (dog*i)%MOD
for j in range(1,M+1):
    monkey = (monkey*j)%MOD

ans =(dog*monkey)%MOD
if N==M:
    ans=(ans*2)%MOD

print(ans)
