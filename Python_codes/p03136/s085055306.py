n = int(input())
l = [int(i) for i in input().split()]
l.sort(reverse = True)
if l[0] < sum(l[1:]):
    print('Yes')
else:
    print('No')