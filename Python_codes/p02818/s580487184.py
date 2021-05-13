import sys
A, B ,K = map(int, input().split())

if A >= K:
    A-=K
    print(A, B)
    sys.exit()
else:
    K -= A
    A = 0

B -= K
if B < 0:
    B = 0
print(A, B)