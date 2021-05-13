N = int(input())
S = input()
ma=0
for i in range(1,N):
    leftS = S[0:i]
    rightS = S[i:]
    setLeftS = set(leftS)
    setRightS = set(rightS)
    m = 0
    for r in setRightS:
        if r in setLeftS:
            m+=1
    ma = max(ma,m)
print(ma)