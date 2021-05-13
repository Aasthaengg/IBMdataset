import sys
from collections import Counter

input = sys.stdin.readline
N = int(input())
S = list(input().strip())
counter = Counter(S)
if len(counter) == 1:
    print(0)
else:
    ans = min(counter["."], counter["#"])
    # 操作後：境界に対して左は白、右は黒になる
    # 境界をどこにするかを全探索
    white = counter["."]
    black = counter["#"]
    left_w = 0
    left_b = 0
    for i in range(N):
        if S[i] == ".":
            left_w += 1
        else:
            left_b += 1
        ans = min(ans, left_b + white - left_w)
    
    print(ans)