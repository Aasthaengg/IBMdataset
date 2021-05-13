l = list(map(int,input().split()))
l = sorted(l)
if l[2] == l[0] + l[1]: print('Yes')
else: print('No')