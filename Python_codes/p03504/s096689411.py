import sys
import heapq  # heapqライブラリのimport

stdin = sys.stdin
 
ri = lambda: int(rs())
rl = lambda: list(map(int, stdin.readline().split()))
rs = lambda: stdin.readline().rstrip()  # ignore trailing spaces

N, C = rl()
STC = [[] for _ in range(C+1)]

for _ in range(N):
    s, t, c = rl()
    STC[c].append((s, t))

for i in range(1, C+1):
    stc = STC[i]
    stc.sort()
    p = []
    for j in range(1, len(stc)):
        if stc[j][0] == stc[j-1][1]:
            stc[j] = (stc[j-1][0], stc[j][1])
            p.append(j-1)
    for x in p[::-1]:
        stc.pop(x)
    STC[i] = stc

program = []
for stc_list in STC:
    for s, t in stc_list:
        program.append((s, t))

program.sort()

recorder = [-1]
heapq.heapify(recorder)

for s, t in program:
    if s-0.5 > recorder[0]:
        heapq.heappop(recorder)
    heapq.heappush(recorder, t)

print(len(recorder))
