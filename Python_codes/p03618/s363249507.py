from collections import Counter
A = input()
n = len(A)
c = Counter(A)

ans = 1
ans += n*(n-1)//2
for v in c.values():
    ans -= v*(v-1)//2
print(ans)
