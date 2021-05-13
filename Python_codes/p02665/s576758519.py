import sys
N = int(input())
A = list(map(int, input().split()))

if N == 0:
    if A[0] == 1:
        print(1)
    else:
        print(-1)
    sys.exit()

capacity = [1 - A[0]]
for i in range(N):
    capacity += [2 * (capacity[-1] - A[i])]


corr_flag = 1
if A[-1] > capacity[-1]:
    corr_flag = 0
curr = A[-1]
ans = A[-1]
for i in range(N-1, -1, -1):
    curr = min(capacity[i], A[i] + curr)
    ans += curr
if corr_flag:
    print(ans)
else:
    print(-1)
