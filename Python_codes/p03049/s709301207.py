N = int(input())
numA = 0
numB = 0
cnt = 0
sm = 0

for i in range(N):
    mm = input()
    if mm[0]=="B":
        numB += 1
    if mm[-1]=="A":
        numA += 1
    if mm[0]=="B" and mm[-1]=="A":
        sm += 1

    for i in range(len(mm)):
        if mm[i:i+2]=="AB":
            cnt += 1

if sm == numA and sm==numB and sm>0:
    numA -= 1
    numB -= 1
mm2 = min(numA,numB,N-1)
print(cnt+mm2)