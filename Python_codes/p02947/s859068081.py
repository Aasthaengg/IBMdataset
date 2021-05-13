from collections import Counter
n = int(input())
s = []
for i in range(n):
    a = list(input())
    s.append("".join(sorted(a)))

c = Counter(s)
ans = 0

for i in c.values():
    #i!/(i-2)!/2!
    ans += int(i*(i-1)/2)

print(ans)
