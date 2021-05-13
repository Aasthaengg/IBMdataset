from collections import Counter

print('Yes' if sorted(list(Counter(input()).values())) == 
       sorted(list(Counter(input()).values())) else 'No')
