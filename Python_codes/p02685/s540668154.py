mod  = 998244353
MAX = 2*10**5 + 100

inv=[0]*(MAX+1)
inv[1]=1
for i in range(2,MAX+1):
    inv[i]=-(mod//i)*inv[mod%i]%mod

g1=[1,1]
g2=[1,1]
for i in range(2,MAX+1):
    num_1=g1[-1]*i%mod
    g1.append(num_1)
    g2.append(g2[-1]*inv[i]%mod)
    
def cmb(n,r):
    return g1[n]*g2[r]*g2[n-r]%mod


N, M, K = map(int,input().split())

ans = 0
for i in range(K+1):
    num = M * pow(M - 1, N - i - 1, mod) % mod
    num = num * cmb(N - 1, i) % mod 
    ans = (ans + num) % mod
    
print(ans)