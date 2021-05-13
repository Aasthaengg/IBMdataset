from collections import Counter
n = int(input())
s = [input() for _ in range(n)]
c = Counter(s)
m = max(c.values())
ans_list = [i for i in c.keys() if c[i]==m]
[print(ans) for ans in sorted(ans_list)]