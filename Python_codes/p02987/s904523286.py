from collections import Counter
S = input()
cnt = Counter(list(S))
print('Yes' if list(cnt.values()) == [2, 2] else 'No')
