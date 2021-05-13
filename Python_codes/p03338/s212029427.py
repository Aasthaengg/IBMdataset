from collections import Counter
n = int(input())
s = list(input())
print(max([len(Counter(s[:i]).keys() & Counter(s[i:]).keys()) for i in range(1,n+1)]))
