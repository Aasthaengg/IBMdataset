l=[list(map(int,input().split()))for i in range(3)]
from itertools import permutations as pe
for i in pe(l,r=None):
    #rは長さ、Noneでiteraterの長さ
    for j in range(2):
        now=i[0][j]
        seen=set([now])
        for a,b in i:

            if b!=now and now!=a:break
            now=b+a-now
            seen.add(now)
        else:
            if len(seen)==4:print('YES');exit()

print("NO")
