import bisect
from itertools import accumulate
X = input()
S = [0]*(len(X))
T = [0]*(len(X))
for i in range(len(X)):
    if X[i] == "S":
        S[i] = 1
    else:
        T[i]=1
Ssum = list(accumulate(S))
Tsum = list(accumulate(T))
kosu=len(X)//2
count=1
for i in range(1,kosu+1):
    Tindex = bisect.bisect_left(Tsum, i)
    if Ssum[Tindex]>=count:
        count+=1
print(len(X)-(count-1)*2)