import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

M,K = map(int,read().split())

if M == 1:
    if K == 0:
        print(0,0,1,1)
    else:
        print(-1)
else:
    if K >= (1<<M):
        print(-1)
    else:
        other = list(range(1<<M)); other.remove(K)
        arr = other + [K] + other[::-1] + [K]
        print(' '.join(map(str,arr)))