class Queue():
    def __init__(self):
        self.l = []
    
    def push(self, e):
        self.l.append(e)
        
    def pop(self):
        return self.l.pop(0)


queue = Queue()
n, q = tuple([int(x) for x in input().split()])
for _ in range(n):
    tmp = input().split()
    queue.push([tmp[0], int(tmp[1])])

time = 0
while queue.l:
    process = queue.pop()
    if process[1] <= q:
        time += process[1]
        print(' '.join([process[0], str(time)]))
    else:
        time += q
        queue.push([process[0], process[1]-q])