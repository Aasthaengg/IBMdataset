abc = list(map(int, input().split()))
if abc[0] <= abc[2] <= abc[1]:
    print('Yes')
else:
    print('No')