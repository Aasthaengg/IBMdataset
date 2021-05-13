H,W,N = map(int,input().split())

from collections import defaultdict
L = defaultdict(int)

#黒く塗りつぶしたマスとその周りだけ探索すればよい
for i in range(N):
    a,b = map(int,input().split())
    for p in [-1,0,1]:
        for q in [-1,0,1]:
            if a+p < 2 or b+q < 2 or a+p >H-1 or b+q >W-1:
                continue
            L[(a+p-1,b+q-1)] += 1
            
ans = [0]*10
for v in L.values():
    ans[v] += 1
ans[0] = (H-2)*(W-2) - sum(ans)

for i in range(10):
    print(ans[i])
