a,b,c,d = map(int,input().split())
if abs(a-c) <= d: print('Yes')
else:
    if a < c:
        if 0 <= b-a <= d and 0 <= c-b <= d: print('Yes')
        else: print('No')
    else:
        if 0 <= a-b <= d and 0 <= b-c <= d: print('Yes')
        else: print('No')
