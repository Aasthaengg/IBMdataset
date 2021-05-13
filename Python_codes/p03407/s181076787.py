A, B, C = map(int, input().split())
ans = A + B - C

if ans >= 0:
    print('Yes')
else:
    print('No')