class ProcessQueue:
    def __init__(self, N):
        self.MAX = N + 1
        self.Q = [(None, None)] * self.MAX
        self.head = 0
        self.tail = 0

    def isEmpty(self):
        return self.head == self.tail

    def enqueue(self, p):
        self.Q[self.tail] = p
        self.tail += 1
        if self.tail == self.MAX:
            self.tail = 0

    def dequeue(self):
        self.head += 1
        if self.head == self.MAX:
            self.head = 0

        return self.Q[self.head - 1]


N, Q = (int(n) for n in input().split())
processes = ProcessQueue(N)
for i in range(N):
    process = input().split()
    processes.enqueue((process[0], int(process[1])))

time = 0
while not processes.isEmpty():
    process = processes.dequeue()
    if process[1] - Q <= 0:
        time += process[1]
        print(process[0], time)
    else:
        time += Q
        processes.enqueue((process[0], process[1] - Q))

