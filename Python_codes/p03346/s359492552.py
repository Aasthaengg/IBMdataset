import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
p = [[int(j),i] for i,j in enumerate(read().split()) ]
p.sort()

longest = 1
now = 1
for i in range(1,n):
    if(p[i][1] > p[i-1][1]):
        now += 1
    else:
        now = 1
    longest = max(longest,now)

print(n-longest)