import sys
def I(): return int(sys.stdin.readline().rstrip())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし

N = I()
S = LS2()

ANS = [0]
for i in range(N):
    if S[i] == 'I':
        ANS.append(ANS[-1]+1)
    else:
        ANS.append(ANS[-1]-1)

print(max(ANS))