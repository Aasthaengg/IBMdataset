import collections
n,cc = int(raw_input()), collections.Counter(raw_input())
print 'Yes' if cc['R'] > cc['B'] else 'No'