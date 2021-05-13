N, Q = map(int, input().split())
S = input()

LR = [list(map(int, input().split())) for _ in range(Q)]

cnt_lst = [0]
cnt = 0
for i in range(1, N):
    if S[i - 1] == 'A' and S[i] == 'C':
        cnt += 1

    cnt_lst.append(cnt)


for l, r in LR:
    print(cnt_lst[r - 1] - cnt_lst[l - 1])
