# A - Airport Bus

N, C, K = map(int, input().split())
T = [int(input()) for i in range(N)]
T.sort()
ans = 0
c = 0
dead_time = 0

for i in range(N):
    if c==0 or T[i]>dead_time:
        dead_time = T[i]+K
        ans += 1
        c = 0
    c = (c+1)%C

print(ans)