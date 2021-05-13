from sys import exit
import bisect

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
if sum(A) < sum(B):
    print(-1)
    exit()
L = [a - b for a, b in zip(A, B)]
L.sort()
x = bisect.bisect_left(L, 0)
low = abs(sum(L[:x]))
s = 0
ans = x  
L.reverse()
for l in L:
    if s >= low:
        break
    s += l
    ans += 1
print(ans)
