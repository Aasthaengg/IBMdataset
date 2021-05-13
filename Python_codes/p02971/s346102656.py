N = int(input())
A = [int(input()) for _ in range(N)]

mls = [-1 for _ in range(N+1)]
for i, a in enumerate(A, 1):
    mls[i] = max(mls[i-1], a)

mrs = [-1 for _ in range(N+1)]
for i, a in enumerate(A[::-1], 1):
    mrs[i] = max(mrs[i-1], a)
mrs = mrs[::-1]

for i in range(N):
    print(max(mls[i], mrs[i+1]))
