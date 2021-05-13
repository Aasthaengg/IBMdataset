abc = list(map(int, input().split()))
from collections import Counter
abc2 = Counter(abc).most_common()
print(len(abc2))