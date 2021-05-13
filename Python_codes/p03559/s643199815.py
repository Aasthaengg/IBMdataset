import bisect
import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
cnt = 0
a.sort()
c.sort()
for i in range(n):
    cnt += (bisect.bisect_left(a, b[i])) * (n-bisect.bisect_right(c, b[i]))
print(cnt)