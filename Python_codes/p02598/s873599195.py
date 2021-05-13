import math
N, K = map(int, input().split())
A = list(map(int, input().split()))
X = max(A)
if K == 0:
    print(X)
    exit()
else:
    for i in range(1, math.ceil(math.log2(X)) + 5):
        B = []
        for a in A:
            b = math.ceil(a / X) - 1
            B.append(b)
        B_total = sum(B)
        if B_total > K:
            X += max(A) / pow(2, i)
        else:
            X -= max(A) / pow(2, i)
    print(math.ceil(X))