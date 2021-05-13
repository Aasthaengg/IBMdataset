import bisect

N,X=map(int,input().split())
L=list(map(int,input().split()))
sumL=[0]
for i in range(N):
    sumL.append(sumL[i]+L[i])
print(bisect.bisect_right(sumL,X))