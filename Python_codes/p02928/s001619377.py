N,K = map(int,input().split())
a_ls = list(map(int, input().split()))
i_great = [0] * N
i_greatleft = [0] * N 

for i in range(N):
    for j in range(N):
        if a_ls[i] > a_ls[j]:
            i_great[i] += 1
            if i < j:
                i_greatleft[i] += 1
#print(i_great)
#print(i_greatleft)

ans = 0
mod = 10**9+7
K %= mod
times = ((K*(K-1))//2)%mod

for i in range(N):
    #print('------')
    #print(i)
    ans += (K*i_greatleft[i])%mod
    #print(K*i_greatleft[i])
    ans += (times*i_great[i])%mod
    #print(times*i_great[i])
    ans %= mod

print(ans)
