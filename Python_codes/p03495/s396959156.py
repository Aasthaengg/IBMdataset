import collections

n,k = map(int,input().split())
a = [int(i) for i in input().split()]
b = collections.Counter(a)
c = sorted(b.items(), key=lambda x:x[1])
ans = 0
d = len(c)
i = 0
while d > k:
    d -= 1
    ans += c[i][1]
    i +=1
print(ans)