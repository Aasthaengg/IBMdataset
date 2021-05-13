import sys
S = list(sys.stdin.readline().rstrip())
K = int(sys.stdin.readline().rstrip())
res = []
for k in range(K):
    for i in range(len(S)- k):
        res.append("".join(S[i:i+k+1]))
res = list(set(res))
res.sort()
print(res[K - 1])