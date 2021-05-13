import sys

readline = sys.stdin.buffer.readline
n = int(readline())
A = map(int, readline().split())
mod = 1000000007

caps = [0] * 3
ans = 1
for a in A:
    ans *= caps.count(a)
    # caps[caps.index(a)] += 1
    for i in range(3):
        if caps[i] == a:
            caps[i] += 1
            break
    ans %= mod
print(ans)
