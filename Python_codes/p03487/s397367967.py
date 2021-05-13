from collections import Counter
N = int(input())
a = list(map(int, input().split()))

c = Counter(a)
ans = 0
for i in c.items():
    if i[0] > i[1]:
        ans += i[1]
    else:
        ans += i[1]-i[0]
print(ans)
