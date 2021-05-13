from collections import  Counter
n = int(input())
lst = []
for _ in range(n):
    lst.append(input())

C = Counter(lst)
x = max(C.values())
anslst = []
for k,v in C.items():
    if v == x:
        anslst.append(k)
anslst.sort()
for v in anslst:
    print(v)