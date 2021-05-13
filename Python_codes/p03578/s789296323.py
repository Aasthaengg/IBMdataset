import sys
n = int(input())
D = list(map(int, input().split()))
m = int(input())
T = list(map(int, input().split()))

max_diff = max(D)
difficulty = {}
for d in D:
    try:
        difficulty[d] += 1
    except:
        difficulty[d] = 1

for t in T:
    try:
        difficulty[t] -= 1
    except:
        print('NO')
        sys.exit()
    if difficulty[t] < 0:
        print('NO')
        sys.exit()
print('YES')
