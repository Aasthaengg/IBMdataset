from collections import Counter
n = int(input())
s = Counter([input() for i in range(n)])
max_s = max(s.values()) 
print(*sorted(k for k, v in s.items() if v == max_s), sep='\n')