N = int(input())
D = [int(i) for i in input().split()]
M = int(input())
T = [int(i) for i in input().split()]

if N < M:
    print('NO')
    exit()

from collections import Counter
 
d_count = Counter(D)
t_count = Counter(T)
for k,v in t_count.items():
    if k not in d_count:
        print('NO')
        exit()
    if d_count[k]< v:
        print('NO')
        exit()
print('YES') 