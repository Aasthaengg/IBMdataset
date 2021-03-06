import sys
input = sys.stdin.readline

N, M = map(int, input().split())
cnt = [0]*N

for _ in range(M):
    a, b = map(int, input().split())
    cnt[a-1] += 1
    cnt[b-1] += 1

for i in range(N):
    if cnt[i]%2==1:
        print('NO')
        exit()

print('YES')