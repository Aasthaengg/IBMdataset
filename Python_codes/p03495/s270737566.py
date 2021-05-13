import collections
N,K = map(int,input().split())
A = list(map(int,input().split()))
A = collections.Counter(A)
res = 0
cnt = A.most_common()
if len(cnt) > K:
    for i in range(K,len(cnt)):
        res += cnt[i][1]
print(res)