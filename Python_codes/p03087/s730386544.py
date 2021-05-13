N, Q = map(int, input().split())
S = input()
ac = [0] * (N + 1)
ans = []
for i in range(N):
    ac[i + 1] = ac[i] + (1 if S[i:i+2] == "AC" else 0)
for _ in range(Q):
    l, r = map(int, input().split())
    ans.append(ac[r - 1] - ac[l - 1])
for i in range(Q):
    print(ans[i])
