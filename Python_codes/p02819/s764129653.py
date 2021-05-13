import sys

X = int(sys.stdin.readline())
exists = set()
for i in range(2, X + 10**5 + 1):
    if i in exists:
        continue
    exists.add(i)
    if X <= i:
        # print(exists)
        print(i)
        sys.exit()

    for j in range(i+i, X + 10**5 + 1, i):
        exists.add(j)