import sys
def I():
    return int(sys.stdin.readline().rstrip())

N = I()

if N == 0:
    print(0)
    exit()

ans = ''

r = 0
while N != 0:
    if N % 2 == 1:
        ans = '1' + ans
        N -= (-1)**r
    else:
        ans = '0' + ans
    N //= 2
    r += 1

print(ans)