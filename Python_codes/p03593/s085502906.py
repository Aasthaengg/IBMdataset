from sys import stdin
from collections import Counter
H,W = [int(x) for x in stdin.readline().rstrip().split()]
c = Counter()

for i in range(H):
    c += Counter(list(input()))

rem0 = 0
rem2 = 0

for i in c.values():
    if i % 4 == 0:
        rem0 += 1
    elif i % 4 == 2:
        rem2 += 1

num_v = len(c.values())

f = True
if H % 2 == 0 and W % 2 == 0:
    if rem0 != num_v:
        f = False

elif H % 2 != 0 and W % 2 != 0:
    
    if len([i for i in c.values() if i % 2 != 0]) != 1:
        f = False
        
    if rem2 > (H-1)/2 + (W-1)/2:
        f = False
    
    if num_v-1 != rem0 + rem2:
        f = False
    
else:
    if H % 2 == 0:
        if rem2 > H/2:
            f = False
        if rem2 + rem0 != num_v:
            f = False
            
    if W % 2 == 0:
        if rem2 > W/2:
            f = False
        if rem2 + rem0 != num_v:
            f = False
    
if f:
    print("Yes")
else:
    print("No")