import  sys
from itertools import combinations
n, k = [int(i) for i in sys.stdin.readline().split()]
if (n - 1) * (n - 2) // 2 < k:
    print(-1)
else:
    print(n - 1 + (n - 1) * (n - 2) // 2 - k)
    for i in range(2,n+1):
        print(1, i)
    cnt = 0
    for combi in combinations(range(2,n+1), 2):
        if (n - 1) * (n - 2) // 2 - k == cnt:
            break
        print(combi[0], combi[1])
        cnt += 1