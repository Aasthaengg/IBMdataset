import sys
n, m, k = map(int, input().split())
mod = 998244353

# 隣り合ったブロックを異なる色で塗ると何通りあるか
# 隣り合ったブロック通しで同じ色にする場所をn-1箇所から選ぶ(combination)

# combinationを計算する
def combination(n, r, p):
    if r < 0 or r > n:
        return 0
    r = min(r, n-r)
    return (f[n]*f_inverse[r]*f_inverse[n-r])%p

f = [1, 1] # n!を計算する
f_inverse = [1, 1]# n!の逆元を計算する
n_inverse = [0, 1] # nの逆元
for i in range(2, n+1):
    f.append((f[i-1]*i)%mod)
    n_inverse.append( (-1*(mod//i)*n_inverse[mod%i])%mod )
    f_inverse.append((f_inverse[i-1]*n_inverse[i])%mod)

# c = m * ((m-1)**(n-1))
# L = []
# for i in range(k+1):
#     L.append(c)
#     c=c//(m-1)

def pow_m(k):
    if k == 0:
        return 1
    elif k%2==0:
        return (pow_m(k//2)**2)%mod
    else:
        return (m-1)*(pow_m(k//2)**2)%mod

count = 0
for i in range(k+1):
    # print(count, c, combination(n-1, i, mod))
    count += combination(n-1, i, mod) * m * pow_m(n-1-i)#L[i]
    count %= mod
    
print(count)