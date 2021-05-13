import collections

N,K = map(int,input().split())
A = list(map(int,input().split()))

count = collections.Counter(A)
c = []
for i in count:
    c.append([count[i],i])

c.sort()

l = len(c)
ans = 0
for i in range(0,max(0,l-K),1):
    ans += c[i][0]

print(ans)
