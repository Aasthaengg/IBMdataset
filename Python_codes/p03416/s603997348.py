import sys, math, itertools, collections, bisect 
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

a, b = map(int, input().split())
for i in range(a, b+1):
    num_str = str(i)
    chk = ''.join(list(reversed(num_str)))
    if num_str == chk:
        ans += 1
print(ans)