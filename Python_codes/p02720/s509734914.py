from collections import deque

K = int(input())

ans = []

queue = deque(range(1, 10))

while len(ans) < K:
    n = queue.popleft()
    ans.append(n)
    n_str = str(n)
    p = int(n_str[-1])
    if p - 1 >= 0:
        queue.append(int(n_str+str(p-1)))
    queue.append(int(n_str+str(p)))
    if p + 1 <= 9:
        queue.append(int(n_str+str(p+1)))

print(ans[-1])

