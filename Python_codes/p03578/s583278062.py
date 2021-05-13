N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))
from collections import Counter

c1 = Counter(D)
c2 = Counter(T)
if c1|c2 == c1:
    print('YES')
else:
    print('NO')