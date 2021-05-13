import sys
def input(): return sys.stdin.readline().strip()
def mapint(): return map(int, input().split())
sys.setrecursionlimit(10**9)

S = list(input())[::-1]
slen = len(S)
T = list(input())[::-1]
tlen = len(T)

for i in range(slen):
    for j in range(tlen):
        if i+j>=slen:
            break
        if not (S[i+j]=='?' or S[i+j]==T[j]):
            break
    else:
        for j in range(tlen):
            S[i+j] = T[j]
        S = [s if not s=='?' else 'a' for s in S[::-1]]
        print(''.join(S))
        break
else:
    print('UNRESTORABLE')