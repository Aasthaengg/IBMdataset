import sys

N, K = map(int, sys.stdin.readline().strip().split())
A = list(map(int, sys.stdin.readline().strip().split()))


max_a = max(A)
if K > max_a:
    print("IMPOSSIBLE")
    sys.exit()


A.sort()

diffs = set()
for i in range(N-1):
    diffs.add(A[i+1] - A[i])

if 1 in diffs:
    print("POSSIBLE")
    sys.exit()

for a_i in A:
    if a_i - K in diffs or a_i == K:
        print("POSSIBLE")
        break
else:
    print("IMPOSSIBLE")