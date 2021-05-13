N, K = map(int, input().split())
A = [-1] + list(map(int, input().split()))

id = [-1] * (N + 1)
x = 1
l = 0
a = []
while id[x] == -1:
    a.append(x)
    id[x] = l
    l += 1
    x = A[x]

c = l - id[x]
if K < l:
    print(a[K])
else:
    K -= l
    print(a[id[x] + K % c])
