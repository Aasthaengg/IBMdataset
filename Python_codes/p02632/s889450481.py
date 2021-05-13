import sys

def I(): return int(sys.stdin.readline().rstrip())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

K = I()
n = len(LS2())
mod = 10**9+7

# 完成図は、
# (S[0]以外からなる文字列)S[0](S[1]以外からなる文字列)S[1]…(S[n-1]以外からなる文字列)S[n-1](任意の文字列)
# この表記は一意
# 形式的冪級数で考えると,
# 求めたいものは (1-25x)^(-n)*(1-26x)^(-1) の x^K の係数であり、
# これは、(i+n-1)_C_(n-1)*25^i*26^(K-i) を i=0,…,K にわたって足し合わせたものである

C = [1]
for i in range(1,K+1):
    C.append((C[-1]*(i+n-1)*pow(i,mod-2,mod)) % mod)
# C[i] = (i+n-1)_C_(n-1)

ans = 0
for i in range(K+1):
    ans += C[i]*pow(25,i,mod)*pow(26,K-i,mod)
    ans %= mod

print(ans)