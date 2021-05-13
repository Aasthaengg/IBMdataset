from collections import Counter
n = int(input())
V = list(map(int,input().split()))
E = []
O = []
for i,v in enumerate(V):
    if i%2==0:
        O.append(v)
    else:
        E.append(v)

cO = Counter(O).most_common(); cO.append((-1,0))
cE = Counter(E).most_common(); cE.append((-1,0))
if cO[0][0]==cE[0][0]: 
    ans = min(n-cO[0][1]-cE[1][1], n-cO[1][1]-cE[0][1])
else:
    ans = n-cO[0][1]-cE[0][1]
print(ans)