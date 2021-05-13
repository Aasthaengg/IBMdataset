import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
ans = 1
MOD = 10**9+7
r, g, b = 0, 0, 0

for Ai in A:
    cnt = 0
    
    if r==Ai:
        cnt += 1
    
    if g==Ai:
        cnt += 1
    
    if b==Ai:
        cnt += 1
        
    ans *= cnt
    ans %= MOD
    
    if r==Ai:
        r += 1
    elif g==Ai:
        g += 1
    else:
        b += 1
    
print(ans)