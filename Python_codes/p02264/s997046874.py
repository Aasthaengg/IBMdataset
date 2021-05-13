from collections import deque


n, q = map(int, input().split())
n_t = deque()
for i in range(n):
    s, j = input().split()
    n_t.append([str(s), int(j)])

timer = 0

while n_t:
    s, i = n_t.popleft()
    if i > q:
        i -= q
        timer += q
        n_t.append([s, i])
    else:
        timer += i
        print("{0} {1}".format(s, timer))