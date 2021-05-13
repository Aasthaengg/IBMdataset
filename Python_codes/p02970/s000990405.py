# 初期入力
import math
import sys
input = sys.stdin.readline
N,D = (int(x) for x in input().split())
see_possible =2*D +1
ans =math.ceil(N / see_possible)
print(ans)