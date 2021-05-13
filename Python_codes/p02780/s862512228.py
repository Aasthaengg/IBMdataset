import itertools
n, k = (int(i) for i in input().split())
P = [int(i) for i in input().split()]

probs = list(itertools.accumulate([(1+p)/2 for p in P]))
probs.insert(0,0)

ans = 0

for i in range(n-k+1):
    ans = max(ans, -probs[i]+probs[i+k])

print(ans)
