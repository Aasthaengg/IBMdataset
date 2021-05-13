from math import ceil

N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

"""
操作X: aに1を足す
操作Y: aに2を足す
操作Z: bに1を足す

問題文の操作はXと一致する。
(X = Y + Z)

if Yの回数 <= Zの回数:
    Yes (不足分はXで処理できる)
else:
    No
"""

cnt = 0

for i in range(N):
    a, b = A[i], B[i]

    # 操作Z
    if a > b:
        Z = a - b
        B[i] += Z
        cnt += Z

for i in range(N):
    # 操作Y
    if A[i] < B[i]:
        Y = (B[i] - A[i]) // 2
        A[i] += 2 * Y
        cnt -= Y

        # 操作X
        if A[i] < B[i]:
            A[i] += 2
            B[i] += 1

if cnt <= 0:
    print("Yes")
else:
    print("No")