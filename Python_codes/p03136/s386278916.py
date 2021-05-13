n = int(input())
l = [int(i) for i in input().split()]
L = max(l)

if L < sum(l)-L:
    print('Yes')
else:
    print('No')