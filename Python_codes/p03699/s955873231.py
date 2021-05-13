from itertools import combinations

N = int(input())
a, b = [], []

for i in range(N):
    c = int(input())
    if c % 10 == 0:
        a.append(c)
    else:
        b.append(c)
if len(b) == 0:
    print(0)
else:
    ans = sum(a)
    val = 0
    for i in reversed(range(1, 1+len(b))):
        for j in combinations(b, i):
            val0 = sum(j)
            if val0 % 10 != 0:
                val = max(val0, val)
        if val != 0:
            break
    if val == 0:
        print(0)
    else:
        print(val+ans)
    
