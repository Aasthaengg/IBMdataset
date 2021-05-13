import sys
imput = sys.stdin.readline

N,M = map(int,input().split())
V = [0 for _ in range(N)]
for _ in range(M):
    a,b = map(int,input().split())
    V[a-1] += 1
    V[b-1] += 1
print('YES' if all([v%2==0 for v in V]) else 'NO')