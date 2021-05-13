import itertools
import math
H,W =list(map(int,input().split(" ")))
N = int(input())
As =list(map(int,input().split(" ")))
color = 0
count = 0
ans = [ [0] * W  for _ in range(H)  ]
for h in range(H):
    if h %2 == 0:
        start = 0
        end = W
        step = 1
    else:
        start = W - 1
        end = -1
        step = -1
    for w in range(start,end,step):
        if count == As[color] :
            color += 1
            count = 0
        ans[h][w] = color + 1
        count += 1

for temp in ans:
    print(*temp)