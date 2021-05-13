class Queue:
    def __init__(self,l):
        self.values = []
        self.l = l
        for _ in range(l):
            self.values.append(None)
        self.head = 0
        self.tail = 0
    def inc(self,n):
        if n+1 >= self.l:
            return 0
        else:
            return n+1
    def enqueue(self,v):
        if self.inc(self.head) == self.tail:
            print 'overflow'
            exit()
        self.values[self.head] = v
        self.head = self.inc(self.head)
    def dequeue(self):
        if self.head == self.tail:
            print 'underflow'
            exit()
        v = self.values[self.tail]
        self.tail = self.inc(self.tail)
        return v
    def size(self):
        if self.head >= self.tail:
            return self.head-self.tail
        else:
            self.head + (self.l-self.tail)

n,q = map(int,raw_input().split(' '))
queue = Queue(200000)
for _ in range(n):
    n,t = raw_input().split(' ')
    t = int(t)
    queue.enqueue((n,t))

c = 0
while queue.size()>0:
    n,t = queue.dequeue()
    if t <= q:
        c += t
        print n,c
    else:
        queue.enqueue((n,t-q))
        c += q