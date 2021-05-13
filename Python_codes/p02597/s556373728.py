import queue

N = int(input())
S = list(input())

R, W = queue.PriorityQueue(), queue.PriorityQueue()
for i in range(N):
    if S[i] == 'R':
        R.put(-i)
    else:
        W.put(i)

steps = 0
while True:
    if R.qsize() == 0 or W.qsize() == 0:
        break
    r, w = -R.get(), W.get()
    if r < w:
        break
    steps += 1

print(steps)

