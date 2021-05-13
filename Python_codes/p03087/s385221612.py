N, Q = map(int, input().split())
S = str(input())
cnt = 0
L = []
L.append(0)

for i in range(N-1):
    A = S[i]
    B = S[i + 1]
    if A == "A" and B == "C":
        cnt += 1
    L.append(cnt)

for x in range(Q):
    f, r = map(int, input().split())
    print(L[r-1] - L[f-1])