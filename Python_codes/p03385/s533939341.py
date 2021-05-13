from collections import Counter
s = list(input())
ans = Counter(s)
if ans['a']==1 and ans['b']==1 and ans['c']==1:
    print('Yes')
else:
    print('No')