from collections import Counter

a = input()
n = len(a)
ans = 1 + n * (n-1) // 2
b = Counter(a)

c = list(b.values())
for i in c:
    ans -= (i-1) * i // 2
    
print(ans)