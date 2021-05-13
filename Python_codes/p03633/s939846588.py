"""
すべての秒数の最小公倍数を求める
Gを最大公約数として持つX,Yの最小公倍数はG*X/G*Y/G
"""
def gcd(a,b):
    return a if b==0 else gcd(b,a%b)
N = int(input())
T = [int(input()) for _ in range(N)]
tmp = T[0]
for i in range(1,N):
    t = T[i]
    g = gcd(tmp,t)
    tmp = g*(tmp//g)*(t//g)
print(tmp)
