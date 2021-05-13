from itertools import accumulate

N = int(input())
A = list(map(int, input().split()))

# Aの累積和 (残っている葉の数) の逆
cA = list(accumulate(A[::-1]))[::-1]

if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()
if A[0]:
    print(-1)
    exit()

# 根から頂点数を確定，根は1
B = [1]
P = 1

for i in range(N):
    # 今の頂点数の2倍を超えられない (葉は)
    if B[i] * 2 < A[i + 1]:
        print(-1)
        exit()
    P += min(2 * B[i], cA[i + 1])
    # 今使う個数と，内点の個数
    B.append(min(2 * B[i], cA[i + 1]) - A[i + 1])
    if B[-1] < 0:
        print(-1)
        exit()

print(P)