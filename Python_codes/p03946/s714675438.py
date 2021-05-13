

N,T = map(int, input().split())
As = list(map(int, input().split()))
AsR = As[::-1]
mxs = []
mx = 0
ind = 0
for i, a in enumerate(AsR):
    if a > mx:
        mx = a
        ind = N-i-1
    mxs.append((mx,ind))
pairs = []
for a,mx in zip(As,mxs[::-1]):
    # print(mx[0]-a,mx[1])
    pairs.append((mx[0]-a,mx[1]))
pairs.sort(reverse=True)
mx = pairs[0][0]
from collections import defaultdict
ans = set()
for x, i in pairs:
    if x != mx:break
    ans.add(i)
print(len(ans))