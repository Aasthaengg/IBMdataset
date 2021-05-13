N = int(input())
A = [int(x) for x in input().split()]

max_A = max(A)
min_A = min(A)

# すべて0の場合
if min_A == max_A == 0:
    print(0)

# Aの要素が0以上の値の場合
elif min_A >= 0:
    print(N - 1)
    for i in range(N - 1):
        print(i + 1, i + 2)

# Aの要素が0以下の値の場合
elif max_A <= 0:
    print(N - 1)
    for i in range(N - 1)[::-1]:
        print(i + 2, i + 1)

# Aの要素が正と負の値が混在する場合
else:
    print(2 * N - 1)
    if abs(max_A) >= abs(min_A):
        index = A.index(max_A)
        for i in range(N):
            print(index + 1, i + 1)
        for i in range(N - 1):
            print(i + 1, i + 2)
    else:
        index = A.index(min_A)
        for i in range(N):
            print(index + 1, i + 1)
        for i in range(N - 1)[::-1]:
            print(i + 2, i + 1)
