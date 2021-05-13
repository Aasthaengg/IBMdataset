import sys
input = sys.stdin.readline

N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()
ans = 0
i = 0

while i<N:
    lim = T[i]+K
    ans += 1
    cnt = 0
    
    while i<N and cnt<C and T[i]<=lim:
        i += 1
        cnt += 1
        
print(ans)