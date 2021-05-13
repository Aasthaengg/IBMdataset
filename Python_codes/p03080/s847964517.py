from collections import Counter
n = int(input())
s = input()
c = Counter(s)
print('Yes' if c['R'] > c['B'] else 'No')
