input()
x = list(map(int, input().split()))
if sum(x) > 2*max(x):
    print('Yes')
else:
    print('No')