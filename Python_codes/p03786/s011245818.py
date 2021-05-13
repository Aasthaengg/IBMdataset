from itertools import accumulate

N = int(input())
A = [int(i) for i in input().split()]
A.sort()
Acum = list(accumulate(A))

cnt = [1] * N
for i in range(N-1):
    # Acum[i]がA[i+1]を吸収できるか
    if A[i+1] <= Acum[i] * 2:
        cnt[i+1] += cnt[i]

print(cnt[-1])