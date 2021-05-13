import sys
input = sys.stdin.readline
N, M = map(int, input().split())

lst = [0] * (N + 1)

for _ in range(M):
    a, b = map(int, input().split())
    lst[a] += 1
    lst[b] += 1

for i in lst:
    if i % 2 == 1:
        print ('NO')
        exit()

print ('YES')