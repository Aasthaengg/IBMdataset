N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
count = 0

for i in range(N):
    if A[i] != 0:  # 担当の街
        if B[i] > A[i]:  # 担当の街を全滅させられる
            B[i] -= A[i]
            count += A[i]
        else:  # 担当の街で精一杯
            count += B[i]
            continue
    if A[i+1] < B[i]:  # 隣の街を全滅させられる
        count += A[i+1]
        A[i+1] = 0
    else:  # 隣の街を全滅させられない
        A[i+1] -= B[i]
        count += B[i]

print(count)
