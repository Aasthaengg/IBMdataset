import math
i = ''.join(input().strip().split())
sq = math.sqrt(int(i))
if sq == int(sq):
    print('Yes')
else:
    print('No')
