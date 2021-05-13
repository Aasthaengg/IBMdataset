lis = list(map(int, input().split()))
lis.sort()
if lis[0] == lis[1] and lis[1] != lis[2]:
    print('Yes')
elif lis[1] == lis[2] and lis[0] != lis[1]:
    print('Yes')
else:
    print('No')