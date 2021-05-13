import sys
n = [int(i) for i in input().split()]
if n[0] <= n[2]:
    if n[1] >= n[2]:
        print('Yes')
        sys.exit()
print('No')
