N = int(input())
A = list(map(int, input().split()))

A = sorted(A)

wa = A[0]  # i - 1 までの和
cnt = 1  # i 番目の生き物の 2 倍より小さかったのに、i 番目の生き物を食べれるやつの数
for i in range(1, N):
    if 2 * wa >= A[i]:
        cnt += 1
    else:
        cnt = 1
    wa += A[i]
print(cnt)
