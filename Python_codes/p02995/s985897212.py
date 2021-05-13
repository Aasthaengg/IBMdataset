A,B,C,D = map(int,input().split())
c,d = C,D
count = 0

# CとDの最大公約数をユークリッドの互除法より求め、最小公倍数を導出
while c!=0 and d!=0:
    if c > d:
        c %= d
    else:
        d %= c

gcd = max(c,d)
# B以下の整数からCの倍数とDの倍数の数を引いた数を求める
# A-1に関しても同様の処理を行い、その差が答えとなる
A_prime = A-1
print((B-(B//C+B//D)+(B//(C*D//gcd)))-
     (A_prime-(A_prime//C+A_prime//D)+(A_prime//(C*D//gcd))))