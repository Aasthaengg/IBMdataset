from collections import Counter

n = int(input())
s = [input() for _ in range(n)]
counter = Counter(s)
output = ['AC', 'WA', 'TLE', 'RE']

for key in output:
    print(f'{key} x {counter[key]}')