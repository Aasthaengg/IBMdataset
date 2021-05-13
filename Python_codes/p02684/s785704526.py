N, K = map(int, input().split())
A = list(map(lambda x: int(x)-1, input().split()))
route = [0]
check = {0}
now = 0
while A[now] not in check:
    route.append(A[now])
    check.add(A[now])
    now = A[now]
start = route.index(A[now])
loop = len(route) - start

if K < len(route):
    print(route[K]+1)
else:
    K -= start
    K %= loop
    print(route[start+K]+1)
