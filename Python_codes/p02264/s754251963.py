n,q = map(int, input().split())
MAX = n + 2
Q = [0 for i in range(MAX)]
head = 0
tail = 0

def enqueue(u, t):
    global tail
    Q[tail] = [u, t]
    tail = (tail + 1) % MAX

def dequeue():
    global head
    x,t = Q[head]
    head = (head + 1) %MAX
    return [x,t]
for i in range(n):
    P = list(input().split())
    enqueue(P[0], int(P[1]))

elaps = 0
while head != tail:
    u,t = dequeue()
    c = min(q, t)
    t -= c
    elaps += c
    if t > 0:
        enqueue(u,t)
    else:
        print(u + " " + str(elaps))