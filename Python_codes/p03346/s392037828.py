import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
p = list(map(int,read().split()))
q = [0] * n
for i,p_i in enumerate(p):
    q[p_i-1] = i

longest = 1
now = 1
for i in range(1,n):
    if(q[i] > q[i-1]):
        now += 1
    else:
        now = 1
    longest = max(longest,now)

print(n-longest)