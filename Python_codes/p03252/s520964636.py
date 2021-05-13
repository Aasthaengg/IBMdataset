from collections import Counter as Ct
print('Yes' if sorted(Ct(input()).values()) == sorted(Ct(input()).values()) else 'No')