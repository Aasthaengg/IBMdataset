import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

S = LS2()

ans = 0
for i in range(len(S)-1):
    if S[i+1] != S[i]:
        ans += 1

print(ans)