from collections import deque
n, q = map(int,raw_input().split())
queue = deque([])
for i in range(n):
    queue.append(map(str,raw_input().split()))

queue = deque(map(lambda x : [x[0],int(x[1])], queue)) 

time = 0

while len(queue) > 0:
    xqt = queue.popleft()
    res_time = xqt[1] - q
    if res_time <= 0:
        time = time + xqt[1]
        print xqt[0], time
    else:
        time = time + q
        xqt[1] = res_time
        queue.append(xqt)