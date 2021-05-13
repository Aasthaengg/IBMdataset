#CODE FESTIVAL 2017 qual A
"""
やるか・やらないかだけで、結果的にできるものは同じ。順序に関係はない。
縦・横にいくつ使うかを全探索で求まった。
"""
import sys
readline = sys.stdin.buffer.readline
def even(n): return 1 if n%2==0 else 0

n,m,k = map(int,readline().split())

for i in range(n+1):
    for j in range(m+1):
        dup = i*j*2
        res = i*m + j*n - dup
        if k == res:
            print("Yes")
            exit()

print("No")