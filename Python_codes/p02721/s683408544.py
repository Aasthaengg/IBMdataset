N, K, C = map(int, input().split())
S = input()

cand_l = []
cnt = 0
rest = 0
for i in range(N):
    if S[i] == "o" and rest <= 0 and cnt < K:
        cand_l.append(i + 1)
        rest = C
        cnt += 1
    else:
        rest -= 1

cand_r = []
cnt = 0
rest = 0
for i in reversed(range(N)):
    if S[i] == "o" and rest <= 0 and cnt < K:
        cand_r.append(i + 1)
        rest = C
        cnt += 1
    else:
        rest -= 1

for l, r in zip(cand_l, cand_r[::-1]):
    if l == r:
        print(l)
