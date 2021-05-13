import sys

N = int(sys.stdin.readline().strip())
T = list(map(int, sys.stdin.readline().strip().split()))
A = list(map(int, sys.stdin.readline().strip().split()))

# i番目の山が取りうる高さの下限、上限
cand = [[1, float("inf")] for _ in range(N)]

l_max = 0
for i in range(N):
    if l_max < T[i]:
        l_max = T[i]
        if cand[i][0] > T[i] or cand[i][1] < T[i]:
            # print("here1", cand[i][0], cand[i][1], T[i])
            print(0)
            sys.exit()
        else:
            cand[i] = [T[i], T[i]]

    else:
        cand[i][1] = min(cand[i][1], T[i])

r_max = 0
for i in range(N-1, -1, -1):
    if r_max < A[i]:
        r_max = A[i]
        if cand[i][0] > A[i] or cand[i][1] < A[i]:
            # print("here2", cand[i][0], cand[i][1], A[i])
            print(0)
            sys.exit()
        else:
            cand[i] = [A[i], A[i]]
    else:
        cand[i][1] = min(cand[i][1], A[i])

# print(l_max, r_max)
if l_max != r_max:
    print(0)
else:
    ans = 1
    for h_min, h_max in cand:
        ans *= (h_max - h_min + 1)
        ans %= 10**9 + 7

print(ans)