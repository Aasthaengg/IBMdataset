import collections
n = input()
a = input().strip()
cnter = collections.Counter(a)
print( 'Yes' if cnter['R'] > cnter['B'] else 'No' )