import sys
N = int(sys.stdin.readline().rstrip())
s = []
if N == 0:
    print(0)
    exit()
base = 1
cur = 2
while N != 0:
    r = N % cur
    r = r + cur if r < 0 else r
    if r > 0:
        s.append("1")
        N -= base
    else:
        s.append("0")
    cur *= 2
    base *= -2
print("".join(s[::-1]))