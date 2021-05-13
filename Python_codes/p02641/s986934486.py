from collections import defaultdict
X, N = map(int, input().split())
P = [int(x) for x in input().split()]

if N == 0:
    print(X)
    exit()

d = defaultdict(bool)
for i in P:
    d[i] = True

i = 0
while True:
    if not d[X - i]:
        print(X - i)
        break
    elif not d[X + i]:
        print(X + i)
        break
    else:
        i += 1
