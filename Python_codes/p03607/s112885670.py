import collections

n = int(input())
A = list(int(input()) for i in range(n))

c = collections.Counter(A)

ans = 0

for x in c.values():
    if x % 2 == 1:
        ans += 1

print(ans)
