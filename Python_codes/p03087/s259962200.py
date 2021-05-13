import itertools

N, Q = map(int, input().split())
S = input()

cnt = [0]*N

for i in range(N):
    if i >= N-1:
        continue
    if S[i] == "A":
        if S[i+1] == "C":
            cnt[i+1] = 1

acum = list(itertools.accumulate(cnt))

for j in range(Q):
    l, r = map(int, input().split())
    print(acum[r-1]-acum[l-1])