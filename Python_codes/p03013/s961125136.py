from collections import defaultdict

stairs = []
steps = []
MOD = 1000000007

n, m = map(int, input().split())
stairs = {int(input()):True for _ in range(m)}

step = defaultdict(int)
step[0] = 1

for i in range(n):
    if i in stairs.keys():
        step[i] = 0
    else:
        step[i+1] = (step[i] + step[i+1]) % MOD
        step[i+2] = (step[i] + step[i+2]) % MOD

print(step[n])
