H, N = [int(x) for x in input().split()]
A = list([int(x) for x in input().split()])

if H > sum(A):
    print('No')
else:
    print('Yes')
