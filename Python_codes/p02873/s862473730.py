import sys
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


S = LS2()
N = len(S)+1

ANS = [0]*N
for i in range(N-1):
    if S[i] == '<':
        ANS[i+1] = ANS[i]+1

for i in range(N-2,-1,-1):
    if S[i] == '>':
        ANS[i] = max(ANS[i],ANS[i+1]+1)

print(sum(ANS))
