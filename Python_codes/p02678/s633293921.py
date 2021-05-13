import collections

N, M = map(int, input().split())

route = {}

for i in range(M):
    A, B = map(int, input().split())

    if not A in route:
        route[A] = [B]
    else:
        route[A].append(B)

    if not B in route:
        route[B] = [A]
    else:
        route[B].append(A)

check = {
    1: 0,
}

queue = collections.deque()
queue.append(1)
result = {}

while queue:
    value = queue.popleft()
    for i in route[value]:
        if not i in check:
            queue.append(i)
            check[i] = check[value] + 1
            result[i] = value

if len(result) == N-1:
    print('Yes')
    for i in range(2, N+1):
        print(result[i])
else:
    print('No')
