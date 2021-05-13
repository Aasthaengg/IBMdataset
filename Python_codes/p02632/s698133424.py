import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

K = int(input())
S = str(input())
mod = 10**9+7
lens = len(S)
length = lens+K

L = 1
pow_dic = [0]*(10**6*2+1)
pow_dic[0] = 1
for i in range(1, 10**6*2+1):
    L = L*i%mod
    pow_dic[i] = L%mod
ans = 0
for rest in range(K+1):
    lenall = length-rest-1
    nlens = lens-1
    l = pow_dic[lenall]*pow(pow_dic[lenall-nlens], mod-2, mod)%mod
    r = pow_dic[nlens]
    comb = l*pow(r, mod-2, mod)%mod
    ans += pow(25, K-rest, mod)*pow(26, rest, mod)*comb%mod
    ans %= mod
print(ans%mod)