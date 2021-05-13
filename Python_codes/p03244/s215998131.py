from collections import Counter
n = int(input())
a = list(map(int, input().split()))
odd_common = Counter(a[::2]).most_common()
even_common = Counter(a[1::2]).most_common()
odd_common.append(('', 0))
even_common.append(('', 0))
if odd_common[0][0] != even_common[0][0]:
    print(n - odd_common[0][1] - even_common[0][1])
else:
    b = max(odd_common[0][1] + even_common[1][1], odd_common[1][1] + even_common[0][1])
    print(n - b)