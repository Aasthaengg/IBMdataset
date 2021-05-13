from collections import Counter
n = int(input())
s = list(map(str, input().split()))
s = Counter(s).most_common()
if len(s) == 3:
    print('Three')
else:
    print('Four')