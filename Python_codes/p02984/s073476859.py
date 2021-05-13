import numpy as np

N = int(input())
W = list(map(int, input().split()))

ans = []

ans.append(str(sum(W) - 2 * sum([W[i] for i in range(N) if i % 2 == 1])))

for i in range(1, N):
    ans.append(str( 2*W[i-1] - int(ans[i-1])))

print(" ".join(ans))