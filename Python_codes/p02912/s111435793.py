import queue

n, m = [int(_) for _ in input().split(' ')]
a = [int(_) for _ in input().split(' ')]

q = queue.PriorityQueue()
for i in a:
    q.put(-i)

for _ in range(m):
    i = -(q.get())
    q.put(-(i >> 1))

answer = 0
for _ in range(n):
    answer -= q.get()

print(answer)
