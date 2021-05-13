from heapq import *

n, k = map(int,input().split())
T = [[] for i in range(n)]
for i in range(n):
    t,d = map(int,input().split())
    T[t-1].append(d)
Top = []
for i in range(n):
    if T[i]:
        T[i].sort(reverse=True)
        Top.append((T[i][0],i))
Top.sort(reverse = True)

various = len(Top)


ans = 0
s = 0
sushi = []
heapify(sushi)
l = 0

for j,(t,i) in enumerate(Top[:k]):
    s += t
    if l + j + 1 > k:
        s -= heappop(sushi)
        l -= 1
    for new in T[i][1:]:
        if l + j + 1 >= k:
            s += new
            s -= heappushpop(sushi,new)
        else:
            s += new
            l += 1
            heappush(sushi, new)
    ans = max(ans, s + (j+1)**2)
print(ans)
