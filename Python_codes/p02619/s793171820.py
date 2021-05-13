D = int(input())
C = list(map(int, input().split()))
S = [[] for _ in range(D)]
for i in range(D):
    S[i] = list(map(int, input().split()))
T = [0 for _ in range(D)]
for i in range(D):
    T[i] = int(input())

last = [0 for _ in range(26)]
ans = 0
for i in range(D):
    contest = T[i] - 1
    ans += S[i][contest]
    d = i + 1
    last[contest] = d
    for x in range(26):
        ans -= C[x] * (d - last[x])
    print(ans)