A, B, C = map(int, input().split())

diff = A - B
C = C - diff
if C < 0:
    C = 0

print(C)
