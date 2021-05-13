import sys
def I():
    return int(sys.stdin.readline().rstrip())

N = I()

if N == 0:
    print(0)
    exit()

ANS = []
r = 0
while True:
    for i in range(10**6):
        if -((2*(4**((i+1)//2)-1))//3) <= N <= (4*(4**(i//2)-1))//3+1:
            for _ in range(r-i-1):
                ANS.append('0')
            ANS.append('1')
            r = i
            break
    N -= (-2)**r
    if N == 0:
        for _ in range(r):
            ANS.append('0')
        break

print(''.join(ANS))