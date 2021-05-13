N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

S_ba = []
S_ab = []
for i in range(N):
    if A[i] < B[i]: S_ba.append(B[i] - A[i])
    elif A[i] > B[i]: S_ab.append(A[i] - B[i])

ans = len(S_ba)
now = 0
rem = sum(S_ba)
S_ab.sort(reverse=True)

for i in range(len(S_ab)):
    if rem <= now: break
    now += S_ab[i]
    ans += 1

if rem > sum(S_ab): print(-1)
else: print(ans)
