import collections
N = int(input())
A = list(map(int, input().split()))

x = 0
y = 0
selection = sorted(list(set(A)))[::-1]
c = collections.Counter(A)
for i in selection:
    if c[i] >= 4:
        if x == 0:
            x = i
        if y == 0:
            y = i
    elif c[i] >= 2:
        if x == 0:
            x = i
        elif y == 0:
            y = i
    if x != 0 and y != 0:
        print(x * y)
        exit()

print(x * y)