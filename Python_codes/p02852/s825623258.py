inpl = lambda: list(map(int,input().split()))
N, M = inpl()
S = list(map(int,input()))
steps = [N]
i = N
while i > M:
    prev = i
    i -= M
    while S[i] > 0:
        i += 1
    if i >= prev:
        print(-1)
        exit()
    else:
        steps.append(i)
ans = []
cur = 0
while steps:
    prev = cur
    cur = steps.pop()
    ans.append(cur-prev)
print(' '.join(map(str,ans)))
