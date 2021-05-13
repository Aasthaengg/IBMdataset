import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

S = LS2()
ans = 1000
for i in range(len(S)-2):
    ans = min(ans,abs(753-int(S[i]+S[i+1]+S[i+2])))
print(ans)
