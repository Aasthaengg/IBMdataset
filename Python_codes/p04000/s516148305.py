# python3 (3.4.3)
import sys
input = sys.stdin.readline

# main
from collections import defaultdict
H,W,N = map(int,input().split())
AB = [list(map(int,input().split())) for _ in range(N)]

dic = defaultdict(int)
for a,b in AB:
    for dh in range(3):
        for dw in range(3):
            if 0 < a-dh <= H-2 and 0 < b-dw <= W-2:
                dic[(a-dh,b-dw)] += 1

Ans = [0]*10
total = 0
for v in dic.values():
    Ans[v] += 1
    total += 1

Ans[0] = (H-2)*(W-2) - total

for ans in Ans:
    print(ans)
