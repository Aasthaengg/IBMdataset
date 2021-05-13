N = int(input())
A = [int(input()) for _ in range(N)]

max1 = max(A)
n_max1 = A.count(max1)

# 最大値と等しい値がが2つ以上ある場合
if n_max1 > 1:
    for _ in range(N):
        print(max1)
    exit()

# 最大値と等しい値が1つだけの場合
else:
    max2 = sorted(list(set(A)))[-2]
    for i in range(N):
        if A[i] != max1:
            print(max1)
        else:
            print(max2)
