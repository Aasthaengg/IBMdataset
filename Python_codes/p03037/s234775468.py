N, M = map(int, input().split())
L = []
R = []
for i in range(M):
    tmp = list(map(int, input().split()))
    L.append(tmp[0])
    R.append(tmp[1])

ans = min(R) - max(L) + 1
if ans < 0: ans = 0
print(ans)