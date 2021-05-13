import sys
n = int(input())
print(0)
sys.stdout.flush()
LS = input()
if LS == 'Vacant':
    exit()
print(n-1)
sys.stdout.flush()
if input() == 'Vacant':
    exit()
L = 0
R = n-1
while L != R-1:
    M = (L+R)//2
    if M & 1:
        M += 1
    if M == R:
        M -= 1
    print(M)
    sys.stdout.flush()
    s = input()
    if s == 'Vacant':
        exit()

    if LS == s:
        L = M
    else:
        R = M
