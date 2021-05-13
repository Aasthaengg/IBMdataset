import collections

N, K = map(int, input().split())
A = list(map(int, input().split()))
A = dict(collections.Counter(A))
A = sorted(A.items(), key=lambda x: x[1], reverse=True)

cnt = 0

for i in range(N):
    if len(A) > K:
        cnt += A[-1][1]
        A.pop()
    else:
        break

print(cnt)
