import math
a = list(map(int, input().split()))
if sum(list(map(lambda x:x%2, a))) == 3:
    b = a.pop(a.index(max(a)))
    print(a[0]*a[1]*(math.ceil(b/2) - math.floor(b/2)))
else:
    print(0)