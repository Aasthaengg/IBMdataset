"""
1. The initial character of S is an uppercase A.
2. There is exactly one occurrence of C between the third character from the beginning and the second to last character (inclusive).
3. All letters except the A and C mentioned above are lowercase.
"""
import collections
def f(r): return r[0] == 'A' and  collections.Counter(r[2:-1])['C'] == 1 and  all([l in set(['A', 'C']) or l.lower() ==l for l in r ])

print 'AC' if f(raw_input()) else 'WA'