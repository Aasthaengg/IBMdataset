s = list(map(int, input().split()))
ma = s.index(max(s))

if s.pop(ma) == sum(s):
    print('Yes')
else:
    print('No')


