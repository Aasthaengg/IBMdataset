S = input().rstrip()
P = {"A", "C", "G", "T"}
cnt = 0
res = 0
for s in S:
    if s in P:
        cnt += 1
        res = max(cnt, res)
    else:
        cnt = 0
print(res)