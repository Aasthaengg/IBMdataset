from collections import Counter
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n, *v = map(int, read().split())

odd_c = Counter(v[0::2])
even_c = Counter(v[1::2])

odd_c = odd_c.most_common()
if len(odd_c) == 1:
    odd_c.append((0, 0))
even_c = even_c.most_common()
if len(even_c) == 1:
    even_c.append((0, 0))

if odd_c[0][0] != even_c[0][0]:
    ans = n - (odd_c[0][1] + even_c[0][1])
else:
    ans = n - (max(odd_c[1][1] + even_c[0][1], odd_c[0][1] + even_c[1][1]))
print(ans)
