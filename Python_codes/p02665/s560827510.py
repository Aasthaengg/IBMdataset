import itertools
N = int(input())
A = [int(_) for _ in input().split()]
if A[0] != 0:
    if N == 0 and A[0] == 1:
        print(1)
    else:
        print(-1)
    exit()
ans = 1
n = 1
if A[0] > 1:
    print(-1)
    exit()
cumr = list(itertools.accumulate(A[::-1]))[::-1]
for i in range(1, N + 1):
    minn = n - A[i - 1]
    n = min(2 * minn, cumr[i])
    if n>=minn and n>=A[i]:
        ans += n
    else:
        print(-1)
        exit()
print(ans)
