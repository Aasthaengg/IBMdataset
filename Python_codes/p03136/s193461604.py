input()
x = list(map(int, input().split()))
if sum(x) - max(x) > max(x):
    print('Yes')
else:
    print('No')