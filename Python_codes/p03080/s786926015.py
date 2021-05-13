from collections import Counter
N = int(input())
c = Counter(input())
ans = 'Yes' if c.get('R', 0) > c.get('B', 0) else 'No'
print(ans)
