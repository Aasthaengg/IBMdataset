from collections import Counter
n = int(input())
s = list(input())
count = Counter(s)
ans = 1
for i in count.values():
    ans *= i+1
print((ans-1)%(10**9+7))
    
