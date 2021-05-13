from collections import deque

n, q = map(int, input().split())
a = deque([])
for i in range(n):
    a.append(list(input().split()))

end_time = 0
while len(a):
    e = a.popleft()
    if int(e[1]) - q > 0:
        e[1] = int(e[1]) - q
        a.append(e)
        end_time += q
    else:
        end_time += int(e[1])
        print(e[0], end_time)

