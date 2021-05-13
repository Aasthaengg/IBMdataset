from collections import Counter
a = Counter(list(map(int,input().split()))).most_common()
print(a[1][0])