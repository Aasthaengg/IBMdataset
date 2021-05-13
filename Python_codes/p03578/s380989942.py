import collections

N = int(input())
D = map(int, input().split())
M = int(input())
T = map(int, input().split())

DC = collections.Counter(D)

for t in T:
    if t in DC:
        if DC[t] > 0:
            DC[t] -= 1
            continue

    print('NO')
    break

else:
    print('YES')
