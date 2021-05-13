import sys

Q = int(sys.stdin.readline().strip())
LR = []
for i in range(Q):
    LR.append([int(x) for x in sys.stdin.readline().strip().split()])

N = 10**5+1
Primes = list(range(N+1))
Primes[1] = 0

for p in Primes:
    if p * p > N+1: break
    if p == 0: continue
    for i in range(p + p, N+1, p):
        Primes[i] = 0

primes = [p for p in Primes if p > 0]

likes = []
r = 0
for n in range(N):
    if n%2 == 1 and Primes[n] > 0 and Primes[n//2+1] > 0:
        r += 1
    likes.append(r)

for i in range(Q):
    print(likes[LR[i][1]] - likes[LR[i][0]-1])
