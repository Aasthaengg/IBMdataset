N = int(input())
import collections

Ls = [collections.deque() for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    Ls[a - 1].append(b - 1)
    Ls[b - 1].append(a - 1)

Cs = sorted(map(int, input().split()), reverse=True)
print(sum(Cs) - Cs[0])

sw = [-1] * N
sw[0] = Cs[0]
ct = 1
stk = collections.deque()
stk.appendleft(0)
while len(stk) > 0:
    crN = stk[0]
    if len(Ls[crN]) == 0:
        stk.popleft()
        continue
    nxN = Ls[crN].popleft()
    if sw[nxN] > 0:
        continue
    sw[nxN] = Cs[ct]
    ct += 1
    stk.append(nxN)
print(" ".join(map(str, sw)))