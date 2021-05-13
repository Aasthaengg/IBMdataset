# 入力
N = int(input())
K = int(input())
X = int(input())
Y = int(input())

# NがK以下ならN泊×X円、NがKより大きいなら(K泊×X円)+((N-K)×Y円)
if N <= K:
    print(N * X)
elif N > K:
    print(K * X + (N - K) * Y)
