N = int(input())
X = list(map(int, input().split()))
L = sorted(X[::])

# 偶数この時のlen(L) // 2のとlen(L)-1のどちらかのみ中央値になる
len_X_first = len(X) // 2 - 1
len_X_second = len(X) // 2

for i in X:
    if (L[len_X_first] >= i):
        print(L[len_X_second])
    elif (L[len_X_second] <= i):
        print(L[len_X_first])
