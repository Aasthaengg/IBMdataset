N,M = (int(x) for x in input().split())
Now = [0]*N
maxL = 1
minR = N
for T in range(0,M):
    L,R = (int(x) for x in input().split())
    if maxL<L:
        maxL = L
    if minR>R:
        minR = R
if maxL>minR:
    print(0)
elif maxL==minR:
    print(1)
elif maxL<minR:
    print(minR-maxL+1)