n = int(input())
l = sorted(list(map(int,input().split())),reverse=True)
if l[0]<sum(l[1:]):
    print('Yes')
else:
    print('No')