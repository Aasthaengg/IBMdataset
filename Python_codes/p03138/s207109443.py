import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


N,K = MI()
K += 1
k = K.bit_length()
K_bit = [(K >> i) & 1 for i in range(k)]  # Kのbitのリスト(下から)
A = LI()
A_bit = [[(A[i] >> j) & 1 for j in range(k)] for i in range(N)]  # Aiたちのbitのリスト(下から)

X = [0]*(k+1)  # 下i桁で最適なもの
for i in range(k):
    a = sum(A_bit[j][i] == 0 for j in range(N))  # 0の個数
    X[i+1] = X[i]
    if a >= N//2+1:
        X[i+1] += 2**i


def f(x):
    return sum(x^A[i] for i in range(N))


ans = 0
for i in range(k-1,-1,-1):
    if K_bit[i] == 1:
        ans = max(ans,f(((K >> (i+1)) << (i+1))+X[i]))

print(ans)
