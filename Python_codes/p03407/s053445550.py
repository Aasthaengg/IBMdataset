
l = list(map(int, input().split()))
C = l[-1]
l.pop()

if sum(l) >= C:
    print('Yes')
else:
    print('No')