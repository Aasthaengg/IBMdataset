import sys

s = sys.stdin.buffer.readline().rstrip().decode()
MOD = 2019
ans = [1] + [0 for i in range(MOD)]
t = 1
r = 0
for i in reversed(s):
    r = (r + int(i)*t) % MOD
    t = t*10%2019
    ans[r] += 1
print(sum([m*(m-1)//2 for m in ans]))
