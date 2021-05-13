import sys
input = sys.stdin.readline
a = list(map(int, input().split()))
if a[1] - a[0] == a[2] - a[1]: print("YES")
else: print("NO")