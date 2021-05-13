from collections import Counter

n = int(input())
results = Counter([input() for _ in range(n)])

for status in ['AC', 'WA', 'TLE', 'RE']:
    print(status + ' x ' + str(results[status]))
