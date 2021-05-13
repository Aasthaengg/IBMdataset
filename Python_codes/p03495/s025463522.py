N, K = map(int, input().split())
*A, = map(int, input().split())
l = len(set(A))
if l <= K:
    print(0)
    exit()

dic = {}
for a in A:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
from operator import itemgetter
dic_s = sorted(dic.items(), key=itemgetter(1))
i = 0
ans = 0
while l > K:
    l -= 1
    k, v = dic_s[i]
    ans += v
    i += 1
print(ans)