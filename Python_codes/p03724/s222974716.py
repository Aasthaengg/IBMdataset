
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline

N,M = map(int,readline().split())

cnt = [0]*(N+1)
for m in map(int,read().split()):
    cnt[m] += 1

print('YES' if all(c%2 == 0 for c in cnt) else 'NO')