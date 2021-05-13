from itertools import accumulate


N, *A = map(int, open(0).read().split())
A.sort()
acc = list(accumulate(A))
ans = N
for i in range(N - 1):
    if 3 * acc[i] < acc[i + 1]:
        ans = N - i - 1
print(ans)
