import sys
n = int(sys.stdin.readline().rstrip("\n"))
l = [False]*101
for a in range(1,10):
    for b in range(1,10):
            l[a*b] = True
if l[n]:
    print('Yes')
else:
    print('No')