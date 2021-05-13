import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

tmp = {v: k+1 for k, v in enumerate(A)}
ans = []
for v, k in sorted(tmp.items(), key=lambda x: x[0]):
    ans.append(k)

print(*ans)