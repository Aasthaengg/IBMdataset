n, *a_l= map(int, open(0).read().split())
lovedBy = [[] for _ in range(n)]
for i, a in enumerate(a_l):
    lovedBy[a-1].append(i)
cnt = 0
for i, a in enumerate(a_l):
    if a-1 in lovedBy[i]:
        cnt += 1
print(cnt//2)