import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


n,m = map(int, input().split())

def factor(n, m=None):
    # mを与えると、高々その素因数まで見て、残りは分解せずにそのまま出力する
    arr = {}
    temp = n
    M = int(-(-n**0.5//1))+1
    if m is not None:
        M = min(m+1, M)
    for i in range(2, M):
        if temp%i==0:
            cnt=0
            while temp%i==0:
                cnt+=1
                temp //= i
            arr[i] = cnt

    if temp!=1:
        arr[temp] = 1

    if not arr:
        arr[n] = 1

    return arr

d = factor(m)

M = 10**9+7 # 出力の制限
N = max(d.values())+10+n # 必要なテーブルサイズ

g1 = [None] * (N+1) # 元テーブル
g2 = [None] * (N+1) #逆元テーブル
inverse = [None] * (N+1) #逆元テーブル計算用テーブル
g1[0] = g1[1] = g2[0] = g2[1] = 1
inverse[0], inverse[1] = [0, 1] 

for i in range( 2, N + 1 ):
    g1[i] = ( g1[i-1] * i ) % M 
    inverse[i] = ( -inverse[M % i] * (M//i) ) % M # ai+b==0 mod M <=> i==-b*a^(-1) <=> i^(-1)==-b^(-1)*aより
    g2[i] = (g2[i-1] * inverse[i]) % M 

def cmb(n, r, M):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return (g1[n] * g2[r] * g2[n-r]) % M

if m!=1:
    ans = 1
    for v in d.values():
        ans *= cmb(v+n-1, n-1, M)
        ans %= M
else:
    ans = 1
print(ans%M)