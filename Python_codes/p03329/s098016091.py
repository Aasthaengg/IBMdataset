import sys
sys.setrecursionlimit(10000000)

N = int(open(0).read())
p = [59049, 46656, 7776, 6561, 1296, 729, 216, 81, 36, 9, 6, 1]

mem = [0] * (N+1)
def dp(n):
    global mem
    if n <= 0:
        return 0
    elif mem[n]:
        return mem[n]
    else:
        mem[n] = min([dp(n-x) + 1 for x in p if n - x >= 0])
        return mem[n]
print(dp(N))