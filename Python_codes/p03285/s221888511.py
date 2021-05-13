import sys
n = int(sys.stdin.readline().rstrip("\n"))
l = [False]*101
for a in range(26):
    for b in range(15):
        if 0<(4*a+7*b)<=100:
            l[4*a+7*b] = True
if l[n]:
    print('Yes')
else:
    print('No')