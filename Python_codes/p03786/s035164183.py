from itertools import accumulate


def Li():
    return list(map(int, input().split()))


N = int(input())
A = Li()
A.sort()
Asum = list(accumulate(A))
ans = 0
for i in range(N-1):
    if Asum[i]*2 >= A[i+1]:
        ans += 1
    else:
        ans = 0
print(ans+1)
