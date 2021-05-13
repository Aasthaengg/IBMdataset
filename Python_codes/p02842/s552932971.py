# 三井住友信託銀行プログラミングコンテスト2019: B – Tax Rate
N = int(input())

X = int(N / 1.08)
X_min = int(X * 1.08)
X_max = int((X + 1) * 1.08)

if X_min == N:
    print(X)
elif X_max == N:
    print(X + 1)
else:
    print(':(')