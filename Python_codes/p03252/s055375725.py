from collections import Counter
s=Counter(Counter(input()).values())
t=Counter(Counter(input()).values())
print('Yes' if s==t else 'No')