""" ABC071D
"""

N = int(input())
S = [input() for _ in range(2)]
C = [[0]*N for _ in range(2)]
MOD = 1000000007
pos = 0
ans = 0
if S[0][pos] == S[1][pos]:
    ans = 3
else:
    ans = 6
    pos += 1

while 1:
    if pos >= N:
        break
    if S[0][pos] == S[1][pos]:
        pos += 1
        if pos >= N:
            break
        if S[0][pos] == S[1][pos]:
            ans *= 2
            ans %= MOD
            
        else:
            ans *= 2
            ans %= MOD
            pos += 1
    else:
        pos += 1
        if pos >= N:
            break
        if S[0][pos] == S[1][pos]:
            continue
        else:
            ans *= 3
            ans %= MOD
            pos += 1

print(ans % MOD)