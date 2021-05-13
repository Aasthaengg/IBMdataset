from collections import Counter

N = int(input())
D = list(map(int,input().split()))
M = int(input())
T = list(map(int,input().split()))

d = Counter(D)
flag = True

for t in T:
    if d[t] == 0:
        flag = False
    else:
        d[t] -= 1
print('YES' if flag else 'NO')