import sys
def input(): return sys.stdin.readline().rstrip()
# ----------------------------------------------------------- #

a, b = (int(x) for x in input().split())
d = b - a
ans = d * (d + 1) // 2 - b
print(ans)
