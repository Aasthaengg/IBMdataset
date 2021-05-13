from collections import Counter
n = int(input())
d = [int(x) for x in input().split()]
m = int(input())
t = [int(x) for x in input().split()]

D = Counter(d)
T = Counter(t)

ans = "YES"
for x in T.keys():
    if D[x] < T[x]:
        ans = "NO"
        break

print(ans)