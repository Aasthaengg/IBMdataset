h,w = map(int,input().split())
from collections import Counter
s = [[] for i in range(h)]
for i in range(h):
    s[i] = input()

ss = []
for i in range(h):
    for j in range(w):
        ss.append(s[i][j])
            
b = Counter(ss)
odd = 0
    
if h % 2 == 0 and w % 2 == 0:
    fl = 1
    for i in b:
        if b[i] % 4 != 0:
            fl = 0
            
    if fl == 1:
        print("Yes")
    else:
        print("No")
        
elif h % 2 == 1 and w % 2 == 0:
    flsum = 0
    for i in b:
        flsum += b[i] % 4
        if b[i] % 2 == 1:
            odd += 1
        
    if odd != 0:
        print("No")
    elif flsum >= 0 and flsum <= w:
        print("Yes")
    else:
        print("No")
        
elif h % 2 == 0 and w % 2 == 1:
    flsum = 0
    for i in b:
        flsum += b[i] % 4
        if b[i] % 2 == 1:
            odd += 1
        
    if odd != 0:
        print("No")
    elif flsum >= 0 and flsum <= h:
        print("Yes")
    else:
        print("No")
        
else:
    flsum = 0
    for i in b:
        flsum += b[i] % 4
        if b[i] % 2 == 1:
            odd += 1
        
    if odd != 1:
        print("No")
    elif flsum >= 0 and flsum <= h+w-1:
        print("Yes")
    else:
        print("No")