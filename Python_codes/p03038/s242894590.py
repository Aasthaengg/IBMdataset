n, m = map(int, input().split())
A = list(map(int, input().split()))

B = [[] for _ in range(m)]
for i in range(m):
    B[i] = list(map(int, input().split()))
B.sort(key=lambda x: -x[1])

_A = []
cnt = 0
for i in range(m):
    _A.extend([B[i][1]]*B[i][0])
    cnt += B[i][0]
    if cnt > n:
        break
A += _A
A.sort(reverse=True)
print(sum(A[:n]))