from collections import Counter

N = int(input())
S = list(input().split())

if len(Counter(S)) == 4:
    print('Four')
else:
    print('Three')
