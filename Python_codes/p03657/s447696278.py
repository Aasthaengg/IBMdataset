import sys
 
stdin = sys.stdin

mod = 1000000007
inf = 1 << 60
 
ni = lambda: int(ns())
na = lambda: list(map(int, stdin.readline().split()))
nan = lambda x: [na() for _ in range(x)]
ns = lambda: stdin.readline().rstrip()
nsn = lambda x: [ns() for _ in range(x)]
nas = lambda: stdin.readline().split()

ab = na()
ab.append(ab[0] + ab[1])

flag = False
for i in range(3):
    if ab[i] % 3 == 0:
        flag = True

if flag:
    print("Possible")
else:
    print("Impossible")