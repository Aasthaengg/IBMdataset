import itertools
N, A, B, C = map(int, input().split())
ln = [int(input()) for _ in range(N)]
bit = itertools.product([0, 1, 2, 3], repeat=N)
ans = 10000
for bi in bit:
    cnt = 0
    a = []
    b = []
    c = []
    for i in range(N):
        if bi[i] == 1:
            a.append(ln[i])
        elif bi[i] == 2:
            b.append(ln[i])
        elif bi[i] == 3:
            c.append(ln[i])
    if len(a) == 0 or len(b) == 0 or len(c) == 0:
        continue
    cnt += 10*(max(len(a)-1, 0)+max(len(b)-1, 0)+max(len(c)-1, 0))
    temp = [sum(a), sum(b), sum(c)]
    temp.sort()
    cnt += abs(temp[0]-C) + abs(temp[1]-B) + abs(temp[2]-A)
    ans = min(ans, cnt)
print(ans)
