import sys
N = int(input())
print(0, flush=True)
cond = input()
if cond == 'Vacant':
    sys.exit()

l = 0
r = N-1
while r-l > 3:
    mid = (l+r)//2
    if mid % 2 == 1:
        mid += 1

    print(mid, flush=True)
    I = input()
    if I == 'Vacant':
        sys.exit()
    else:
        if cond == I:
            l = mid
        else:
            r = mid

for i in range(l,r+1):
    print(i, flush=True)
    if input() == 'Vacant':
        sys.exit()
