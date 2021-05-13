import sys
def I():
    return int(sys.stdin.readline().rstrip())

N = I()

L = []
for i in range(N+1):
    if i == 0:
        L.append(2)
    elif i == 1:
        L.append(1)
    else:
        L.append(L[-1]+L[-2])
print(L[-1])