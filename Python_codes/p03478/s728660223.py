import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

n, a, b = map(int, input().split())
for i in range(1, n+1):
    s = str(i)
    chk = 0
    for j in range(len(s)):
        chk += int(s[j])
    if a <= chk and chk <= b:
        ans += i
print(ans)