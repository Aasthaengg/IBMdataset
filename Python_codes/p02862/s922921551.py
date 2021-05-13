import sys
input = lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(max(1000, 10**9))
write = lambda x: sys.stdout.write(x+"\n")


x,y = list(map(int, input().split()))

### 素数の逆元とCombination
M = 10**9+7 # 出力の制限
N = (x+y)//3 * 2 +100 # 必要なテーブルサイズ

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


if (x+y)%3!=0:
    ans = 0
else:
    xy = (x+y)//3
    xx = y - xy
    yy = x - xy
    if xx<0 or yy<0:
        ans = 0
    else:
        ans = cmb(xx+yy, xx, M)
print(ans)