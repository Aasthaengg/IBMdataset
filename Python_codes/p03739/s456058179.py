N = int(input())
A = list(map(int, input().split()))

a0 = A[0]
if a0 > 0:
    S1, cnt1 = a0, 0
    S2, cnt2 = -1, abs(a0) + 1
elif a0 < 0:
    S1, cnt1 = 1, abs(a0) + 1
    S2, cnt2 = a0, 0
else:
    S1, cnt1 = 1, 1
    S2, cnt2 = -1, 1

S = S1
cnt = cnt1
for i in range(1, N):
    nS = S + A[i]
    if S > 0:
        if nS > 0:
            cnt += abs(nS) + 1
            nS = -1
    elif S < 0:
        if nS < 0:
            cnt += abs(nS) + 1
            nS = 1
    S = nS
ans = cnt

S = S2
cnt = cnt2
for i in range(1, N):
    nS = S + A[i]
    if S > 0:
        if nS >= 0:
            cnt += abs(nS) + 1
            nS = -1
    elif S < 0:
        if nS <= 0:
            cnt += abs(nS) + 1
            nS = 1
    S = nS
ans = min(cnt, ans)
print(ans)
