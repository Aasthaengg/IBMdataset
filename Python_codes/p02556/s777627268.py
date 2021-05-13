import sys
readline = sys.stdin.buffer.readline

n = int(readline())
z,w = [],[]
for _ in range(n):
    x, y = map(int,readline().split())
    z.append(x+y)
    w.append(x-y)

z.sort()
w.sort()

print(max(z[n-1]-z[0],w[n-1]-w[0]))

