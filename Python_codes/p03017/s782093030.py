import re
n, a, b, c, d = map(int, input().split())
road = input()
if c < d:
    if re.search('##', road[a:d]) is None:
        print('Yes')
    else:
        print('No')
 
elif c > d:
    if re.search('##', road[a:]) is None and re.search('\.\.\.', road[b-2:d+1]) is not None:
        print('Yes')
    else:
        print('No')