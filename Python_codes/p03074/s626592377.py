N, K = map(int, input().split())
S = input().rstrip()
s0 = S[0]
cnt = 1
d = []
for s in S[1:]+"2":
    if s == s0:
        cnt += 1
    else:
        d.append(cnt)
        cnt = 1
    s0 = s
if S[0] == "0":
    d = [0] + d
if S[-1] == "0":
    d += [0]
L = len(d)
if L//2 < K:
    print(sum(d))
else:
    S = sum(d[:2*K+1])
    res = S
    for i in range(2,L-2*K+1,2):
        S = S - d[i-2] - d[i-1] + d[2*K+i-1] + d[2*K+i]
        res = max(S,res)
    print(res)