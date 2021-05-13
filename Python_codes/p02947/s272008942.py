import collections
n = int(input())

s = ["".join(sorted(input())) for i in range(n)]

a = collections.Counter(s)

ans = 0

for i in a.values():
    ans += i*(i-1)//2

print(ans)
