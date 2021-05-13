from collections import Counter
N = int(input())
A = list(map(int,input().split()))
count = Counter(A)
keys = list(count.keys())
keys.sort(reverse = True)
a = 0
b = 0
for k in keys:
    if a == 0:
        if count[k] >= 4:
            a = b = k
            break
        elif count[k] >= 2:
            a = k
    else:
        if count[k] >= 2:
            b = k
            break
print(a * b)