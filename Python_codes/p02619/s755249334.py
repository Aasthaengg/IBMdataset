D = int(input())
C = [0] + list(map(int, input().split())) # type_iのvの下がりやすさ = C[i]
S = [0] + [[0] + list(map(int, input().split())) for _ in range(D)]

T = [0] + [int(input()) for _ in range(D)]
last = [0] + [0 for _ in range(26)]

v = 0 # 現在の満足度
for d in range(1, 1+D): # d = 1, 2, ..., Dについて
    v += S[d][T[d]] # s_di満足度が増える
    last[T[d]] = d # type_T[d]を開催した最後の日をdに設定
    # 満足度現象の計算
    for i in range(1, 27): # type1～27まで
        v -= C[i] * (d - last[i])
    print(v)