n = int(input())
s = list(map(str, input().split()))
import collections
s = collections.Counter(s)

if len(s)==4:
    print('Four')
else:
    print('Three')