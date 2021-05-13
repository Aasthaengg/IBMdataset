n,k=map(int,input().split())
a=list(map(int,input().split()))


mod=pow(10,9)+7

def cmb(n, r, mod):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % mod
N = n
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル
for i in range( 2, N + 1 ):
    g1.append( ( g1[-1] * i ) % mod )
    inverse.append( ( -inverse[mod % i] * (mod//i) ) % mod )
    g2.append( (g2[-1] * inverse[-1]) % mod )

from collections import Counter
cnt_a=Counter(a)
list_a=list(cnt_a.keys())
list_a.sort()
num_a=len(list_a)
sa_=0
sa=[0]
for ai in list_a:
    sa_+=cnt_a[ai]
    sa.append(sa_)
ansmin=0
ansmax=0
for i in range(num_a):# list_a[i]がminになる場合の数
    k_=sa[num_a]-sa[i]
    if k_>=k:
        mi=0 if k_-cnt_a[list_a[i]]<k else cmb(k_-cnt_a[list_a[i]],k,mod)
        ansmin+=list_a[i]*(cmb(k_,k,mod)-mi)
        ansmin%=mod
for i in range(num_a):# list_a[i]がmaxになる場合の数
    k_=sa[i+1]
    if k_>=k:
        mi=0 if k_-cnt_a[list_a[i]]<k else cmb(k_-cnt_a[list_a[i]],k,mod)
        ansmax+=list_a[i]*(cmb(k_,k,mod)-mi)
        ansmax%=mod
print((ansmax-ansmin)%mod)
