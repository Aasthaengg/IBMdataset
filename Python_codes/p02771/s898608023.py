from collections import Counter
abc = Counter(list(map(int, input().split()))).most_common()
if len(abc) == 2:
    print('Yes')
else:
    print('No')