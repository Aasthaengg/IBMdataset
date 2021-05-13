import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


M = 10**9+7 # 出力の制限
N = 10**4 # 必要なテーブルサイズ

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

n,p = map(int, input().split())
a = list(map(int, input().split()))

N = 50
f = [None]*N
v = 1
for i in range(N):
    f[i] = v
    v *= (i+1)
def cmb(n, r, M=None):
    return (f[n] // f[r] // f[n-r])

n0 = sum(num%2==0 for num in a)
n1 = sum(num%2==1 for num in a)
ans = 0
if p==1:
    for i1 in range(1, n1+1, 2):
        ans += cmb(n1, i1)
else:
    for i1 in range(0, n1+1, 2):
        ans += cmb(n1, i1)
ans *= pow(2, n0)
print(ans)