import sys
def I(): return int(sys.stdin.readline().rstrip())


S = I()
mod = 10**9+7
ANS = [1,0,0]
for _ in range(S-2):
    ANS.append((ANS[-1]+ANS[-3]) % mod)

print(ANS[S])
