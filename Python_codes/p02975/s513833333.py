from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
dd = defaultdict(int)

for num in a:
    dd[num] += 1
    if len(dd) >= 4:
        print("No")
        exit()

if len(dd) == 1:    
    if dd[0] > 0:
        print("Yes")
    else:
        print("No")
    exit()

if n % 3 != 0:
    print("No")
    exit()
    
    
if len(dd) == 2:
    if dd[0] == n // 3:
        print("Yes")
    else:
        print("No")
        
else:
    lst = []
    for i, j in dd.items():
        lst.append(i)
        if j != n // 3:
            print("No")
            exit()
    if lst[0] ^ lst[1] ^ lst[2] == 0:
        print("Yes")
    else:
        print("No")
