N = int(input())
import collections

Ls = [[] for _ in range(N)]
for _ in range(N - 1):
    a, b = map(int, input().split())
    Ls[a - 1].append(b - 1)
    Ls[b - 1].append(a - 1)

Cs = sorted(map(int, input().split()))
print(sum(Cs) - max(Cs))

sw = [-1] * N
stk = collections.deque([0])
while len(stk) > 0:
    crN = stk.popleft()
    if sw[crN] < 0:
        sw[crN] = Cs.pop()
        for l in Ls[crN]:
            stk.append(l)

print(*sw)