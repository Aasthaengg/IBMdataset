import sys

def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

S = LS2()
n = len(S)

ans = 0
for i in range(n//2):
    if S[i] != S[n-1-i]:
        ans += 1

print(ans)