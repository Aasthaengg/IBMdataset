N = int(input())
L = list(map(int, input().split()))
L.sort()
x = L[-1]
L = L[:-1]
if sum(L) > x:
    print('Yes')
else:
    print('No')