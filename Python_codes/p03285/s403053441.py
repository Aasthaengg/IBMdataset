n = int(input())
if n in set([4*i+7*j for i in range(100//4+1) for j in range(100//7+1) if (4*i+7*j)<=100]):
    print('Yes')
else:
    print('No')