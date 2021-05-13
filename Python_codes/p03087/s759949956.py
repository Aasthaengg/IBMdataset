N, Q = map(int, input().split())
S = input()
qn = [list(map(int, input().split())) for _ in range(Q)]
cnt = [0 for _ in range(N+10)]
for i in range(1, N+1):
    if (S[i-1:i+1] == "AC"):
        cnt[i] = cnt[i-1] + 1
    else:
        cnt[i] = cnt[i-1]
for q in qn:
    l, r = q
    print(cnt[r-1] - cnt[l-1])








