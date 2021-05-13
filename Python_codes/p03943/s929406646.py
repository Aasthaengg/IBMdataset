a = [int(i) for i in input().split()]
if max(a) == (sum(a)-max(a)):
    print('Yes')
else:
    print('No')