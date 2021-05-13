N, Q = map(int, input().split())
S = input().rstrip()
cnt = 0
tmp = 0
res = [0]*N
for i, s in enumerate(S):
    if s == "A":
        tmp = 1
    elif s=="C" and tmp == 1:
        tmp = 0
        cnt += 1
    else:
        tmp = 0
    res[i] = cnt
for _ in range(Q):
    l, r = map(int, input().split())
    l -= 1
    r -= 1
    print(res[r] - res[l])