m, s, mps = [int(x) for x in input().split()]
time = m / mps

if s >= time:
    print('Yes')
else:
    print('No')