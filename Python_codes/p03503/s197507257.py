from sys import stdin
import itertools

N = int(stdin.readline().rstrip())
F = []

for i in range(N):
    f = [int(x) for x in stdin.readline().rstrip().split()]
    F.append(f)
    
P = []
for i in range(N):
    p = [int(x) for x in stdin.readline().rstrip().split()]
    P.append(p)

ans = -10**9
for i in itertools.product([0,1],repeat=10):
    if sum(i) == 0:
        continue
    score = 0
    for ind,f in enumerate(F):
        num = sum([j*k for j,k in zip(i,f)])
        score += P[ind][num]
    ans = max(ans,score)
    
print(ans)