n = int(input())
a1 = [int(input()) for i in range(n)]
from collections import Counter
a = Counter(a1).most_common()
num = 0
for i in range(len(a)):
    if a[i][1]%2 == 1:
        num += 1
print(num)