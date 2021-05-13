from collections import Counter
s = Counter(input()).most_common()
if len(s) == 2 and s[0][1] == 2:
    print('Yes')
else:
    print('No')