l = list(map(int,input().split()))
l.sort(reverse=1)
if l[0] == l[1]+l[2]: print('Yes')
else: print('No')
