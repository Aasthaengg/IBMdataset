#22 C - Guess The Number
N,M = map(int,input().split())

sc = []
for _ in range(M):
    s,c = map(int,input().split())
    sc.append((s,c))
sc = list(set(sc))

ans = [0]*N
for i, j in sc:
    if ans[i-1] != 0:
        result = -1
        break
    ans[i-1] = j
else:
    if ans[0] == 0:
        ans[0] = 1
    ans = [str(k) for k in ans]
    result = ''.join(ans)
if (1,0) in set(sc):
    result = -1
if N == 1 and M == 1 and sc == [(1,0)]:
    result = 0
if N == 1 and M == 0:
    result = 0
print(result)