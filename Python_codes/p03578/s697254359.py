from collections import Counter

N = int(input())
D = Counter(map(int, input().split()))
M = int(input())
*T, = map(int, input().split())


for t in T:
    if D[t]:
        D[t] -= 1
    else:
        print('NO')
        break
else:
    print('YES')
