from collections import Counter
s = Counter(input()).values()
print("Yes" if min(s)==max(s) and len(s)==2 else "No")