from collections import Counter

N = int(input())
A = list(map(int,input().split()))

c = list(Counter(A).items())
ans = len(c)
even = 0
for x, y in c:
    if y % 2 == 0:
        even += 1
if even % 2 == 0:
    pass
else:
    ans -= 1
print(ans)