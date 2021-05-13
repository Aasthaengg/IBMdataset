from collections import Counter
n = int(input())
a = [int(i) for i in input().split()]
c = Counter(a)
flag = False

if c[0] == n:
    flag = True
elif c[0] == n/3 and len(c) == 2:
    flag = True
else:
    s = 0
    for num in c:
        s ^= num
        if c[num] != n/3: break
    else:
        if s == 0: flag = True

print("Yes" if flag else "No")