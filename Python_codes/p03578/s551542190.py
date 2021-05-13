#38 B - Problem Set
import collections
N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

cntD = collections.Counter(D)
cntT = collections.Counter(T)

result = 'YES'
for t in cntT.keys():
    if not(t in cntD):
        result = 'NO'
        break
    if cntT[t] > cntD[t]:
        result = 'NO'
        break
print(result)