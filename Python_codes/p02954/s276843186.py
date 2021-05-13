import bisect

S = input()
N = len(S)

ans = [0] * N
R = []

for i in range(1, N):
    if S[i-1] == "R" and S[i] == "L":
        R.append(i-1)

for i in range(N):
    idx = bisect.bisect_left(R, i)
    if S[i] == "R":
        if (R[idx] - i) % 2 == 0:
            ans[R[idx]] += 1
        else:
            ans[R[idx]+1] += 1
    else:
        if (i - R[idx-1]) % 2 == 0:
            ans[R[idx-1]] += 1
        else:
            ans[R[idx-1]+1] += 1

print(*ans)