import collections
N = int(input())
A = list(map(int,input().split()))
A_col = collections.Counter(A)
length = []
for k,v in A_col.items():
    if v >= 4:
        length.append(k)
    if v >= 2:
        length.append(k)
length.sort()
if len(length) <= 1:
    print(0)
else:
    print(length[-1]*length[-2])