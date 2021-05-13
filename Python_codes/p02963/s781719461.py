import sys
input = lambda : sys.stdin.readline().rstrip()

import sys
sys.setrecursionlimit(max(1000, 10**9))


s = int(input())
x1, y1 = 0, 0
# k : k*k <= sである最大のk
k = int(s**0.5) - 2
while k<0 or k*k<s:
    k += 1
k -= 1

if k*k==s:
    x2, y3 = k, k
    x3, y2 = 0, 0
elif k*(k+1)>=s:
    x2, y3 = k, k+1
    x3, y2 = 1, (x2*y3 - s)
else:
    x2, y3 = k+1, k+1
    x3, y2 = 1, (x2*y3 - s)
print(" ".join(map(lambda x: str(int(x)), [x1, y1, x2, y2, x3, y3])))