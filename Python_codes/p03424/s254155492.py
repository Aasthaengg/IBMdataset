from collections import Counter
n = int(input())
S = Counter(input().split())
print('Four' if len(S) == 4 else 'Three')