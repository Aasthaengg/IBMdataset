import sys
import math
input = sys.stdin.readline
ins = lambda: input().rstrip()
ini = lambda: int(input().rstrip())
inm = lambda: map(int, input().split())
inl = lambda: list(map(int, input().split()))

n = ini()
count = n
ans = 1
while count != 0:
    count = (count + n) % 360
    ans += 1
print(ans)