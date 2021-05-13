import collections


N = int(input())
A = [int(x) for x in input().split()]

c = collections.Counter(A)

ans = 0
for k in c.keys():
    if k <= c[k]:
        ans += c[k] - k
    else:
        ans += c[k]

print(ans)



