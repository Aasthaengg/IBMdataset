import sys
input = sys.stdin.readline
N = int(input())
A = [int(input()) for _ in range(N)]

odd = sum(a % 2 == 1 for a in A)

if odd == 0:
    ans = "second"
else:
    ans = "first"

print(ans)
