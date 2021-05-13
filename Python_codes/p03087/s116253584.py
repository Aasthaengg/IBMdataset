N, Q = map(int, input().split())
S = input()

ac_cnt = [0] * N
for i in range(1, N):
    if S[i-1:i+1] == 'AC':
        ac_cnt[i] = ac_cnt[i-1] + 1
    else:
        ac_cnt[i] = ac_cnt[i-1]

for _ in range(Q):
    l, r = map(int, input().split())
    ans = ac_cnt[r-1] - ac_cnt[l-1]
    print(ans)