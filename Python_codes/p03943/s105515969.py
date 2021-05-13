a = sorted(list(map(int, input().split())))
if a[-1] == sum(a[:2]): print('Yes')
else: print('No')

