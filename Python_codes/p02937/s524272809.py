import sys

numChar = 26
ordA = ord('a')

Ss = input().rstrip()
Ts = input().rstrip()

setS, setT = set(Ss), set(Ts)
for T in setT:
    if T not in setS:
        print(-1)
        sys.exit()

def getDistNextss(As, numChar):
    lenA = len(As)
    poss = [-1] * numChar
    for i, A in enumerate(As):
        if poss[A] == -1:
            poss[A] = i + lenA
    distNextss = [[0]*(numChar) for _ in range(lenA)]
    for i in reversed(range(lenA)):
        poss[As[i]] = i
        distNextss[i] = [pos-i for pos in poss]
    return distNextss

As = [ord(S)-ordA for S in Ss]
distNextss = getDistNextss(As, numChar)

lenS = len(Ss)
i = 0
for T in Ts:
    T = ord(T) - ordA
    i += distNextss[i%lenS][T]
    i += 1

print(i)
