import sys
readline = sys.stdin.readline

K = int(readline())
S = readline().rstrip()
S = len(S)
N = K + S

DIV = 10 ** 9 + 7
n = (10 ** 6) * 2
g1 = [1, 1] # 元テーブル
g2 = [1, 1] #逆元テーブル
inverse = [0, 1] #逆元テーブル計算用テーブル

for i in range( 2, n + 1 ):
    g1.append( ( g1[-1] * i ) % DIV )
    inverse.append( ( -inverse[DIV % i] * (DIV//i) ) % DIV )
    g2.append( (g2[-1] * inverse[-1]) % DIV )

def nCr(n, r, DIV):
    if ( r<0 or r>n ):
        return 0
    r = min(r, n-r)
    return g1[n] * g2[r] * g2[n-r] % DIV

# K = 3, S = 5のとき
# ..X.X.X.
# Xが取る3か所を選んだ上で、
# 最も右のXよりも右のマス：各26通り
# 最も右のXを含む、それより左のマス：Xのマスは1通り、それ以外は各25通り
# 最も右のXが
# ..X.....　の状態から、
# .......X  
# の状態について、場合の数を求める

ans = 0
for xpos in range(S, N + 1):
  # xpos箇所からK箇所を選ぶ場合の数
  # 一番右に1個固定した状態で、残りのxpos - 1か所からS - 1個を選ぶ
  pat = nCr(xpos - 1, S - 1, DIV)
  # その場合の数に対して、X以外の文字の選び方は25 ** (X - S)通りある
  pat *= pow(25, xpos - S, DIV)
  pat %= DIV
  
  # 残りのマスに対しては26通りずつ選べる
  pat *= pow(26, N - xpos, DIV)
  pat %= DIV
  
  ans += pat
  ans %= DIV

print(ans)
