import sys
input = sys.stdin.readline

N, C, K = map(int, input().split())
T = [int(input()) for _ in range(N)]
T.sort()
now = 0
ans = 0

while now<N:
    ans += 1
    lim = T[now]+K
    
    for _ in range(C):
        if T[now]<=lim:
            now += 1
        else:
            break
        
        if now==N:
            break

print(ans)