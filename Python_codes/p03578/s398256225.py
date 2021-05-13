from collections import defaultdict

N = int(input())
D = list(map(int, input().split()))
M = int(input())
T = list(map(int, input().split()))

if N < M:
    print('NO')
    exit()

dic = defaultdict(int)

for d in D:
    dic[d] += 1

for t in T:
    dic[t] -= 1
    if dic[t] < 0:
        print('NO')
        exit()
print('YES')