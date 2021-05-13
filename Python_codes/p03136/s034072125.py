N = int(input())
L = sorted([int(X) for X in input().split()])
if sum(L[:-1])>L[-1]: print('Yes')
else: print('No')