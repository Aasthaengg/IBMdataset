import sys, bisect

N = int(input())
L = list(map(int, sys.stdin.readline().rsplit()))
L.sort()

res = 0
for i in reversed(range(1, N)):
    for j in reversed(range(i)):
        r = bisect.bisect_right(L, abs(L[i] - L[j]))
        
        if r < j:
            res += j - r
        
print(res)
