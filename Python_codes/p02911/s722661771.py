import sys
from collections import Counter
N, K, Q = map(int, input().split())

result = ["No"]*N
Npoint = [K-Q]*N

Alist = [int(input())-1 for _ in range(Q)]

if K > Q:
    for _ in range(N):
        print("Yes")
    sys.exit()

Alist = Counter(Alist)

for k, v in Alist.items():
    Npoint[k] += v
    if Npoint[k] >= 1:
        result[k] = "Yes"

for i in result:
    print(i)
