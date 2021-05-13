from collections import Counter
n = int(input())
s = [str(input()) for i in range(n)]
s = Counter(s).most_common()
print(len(s))