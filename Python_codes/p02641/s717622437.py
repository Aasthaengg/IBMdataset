import sys
X, N = map(int, input().split())
P = list(map(int, input().split()))

abs_list = []

if N == 0:
    print(X)
    sys.exit()

for i in range(0,150):
    j,k = abs(X - i), X +i
    if j not in P:
        print(j)
        break
    if k not in P:
        print(k)
        break