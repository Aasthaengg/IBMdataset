import collections
N,K = map(int,input().split())
A = list(map(int,input().split()))
c = collections.Counter(A)
count = c.most_common()[::-1]

n = len(count)-K
cnt = 0
for i in range(n):
    cnt += count[i][1]
print(cnt)