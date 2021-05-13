from collections import  defaultdict


N = int(input())

d = defaultdict(int)
for i in range(1, N+1):
    s = str(i)
    d[(s[0], s[-1])] += 1


ans = 0
for i in range(1,N+1):
    s = str(i)
    ans += d[(s[-1], s[0])]


print(ans)