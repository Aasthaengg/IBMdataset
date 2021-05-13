import sys, math, itertools, collections, bisect
input = lambda: sys.stdin.buffer.readline().rstrip().decode('utf-8') 
inf = float('inf') ;mod = 10**9+7 
mans = inf ;ans = 0 ;count = 0 ;pro = 1

s = input()
now = 100000000000
for i in range(len(s)-2):
    chk = abs(753 - int(s[i:i+3]))
    if i == 0:
        now = chk
    elif chk < now:
        now = chk
print(now)