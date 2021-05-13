s = str(input())
s1 = [s[i] for i in range(4)]
from collections import Counter
s2 = Counter(s1).most_common(2)
if s2[0][1] == 2 and s2[1][1] == 2:
    print('Yes')
else:
    print('No')