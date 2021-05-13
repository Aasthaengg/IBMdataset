N, M = map(int, input().split())
*A, = map(int, input().split())

import collections
dic = collections.Counter(A)

for _ in range(M):
    b, c = map(int, input().split())
    if c in dic:
        dic[c] += b
    else:
        dic[c] = b

ans, k = 0, 0
l = sorted(list(dic.keys()), key=lambda x: -x)
for a in l:
    if k + dic[a]<= N:      
        k += dic[a]  
        ans += a*dic[a]
    else:
        ans += a*(N-k)
        break

print(ans)