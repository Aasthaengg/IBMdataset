4
'RRBR'

n = raw_input()
import collections
cc = collections.Counter(raw_input())
print 'Yes' if cc['R'] > cc['B'] else 'No'