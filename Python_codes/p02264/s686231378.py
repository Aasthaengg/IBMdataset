import collections
n, q = map(int, input().split())
P = collections.deque()
for _ in range(n):
    name, time = input().split()
    P.append([name, int(time)])

total_time = 0
while P:
    name, time = P.popleft()
    if time <= q:
        total_time += time
        print(name, total_time)
    else:
        time -= q
        total_time += q
        P.append([name, time])