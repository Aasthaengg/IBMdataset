# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=ALDS1_3_B
# Queue
# Result:
import sys

class Process:
    def __init__(self, name, time):
        self.name = name
        self.time = time

    def __str__(self):
        return '%s(%d)' % (self.name, self.time)


class Queue:
    def __init__(self):
        self.store = []

    def __str__(self):
        """From head to tail"""
        str_val = ''
        for var in self.store:
            str_val += str(var) + '\n'
        return str_val.rstrip()

    def enqueue(self, v):
        self.store.append(v)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.store.pop(0)

    def is_empty(self):
        if len(self.store) == 0:
            return True
        else:
            return False


### main
vals = sys.stdin.readline().rstrip().split(' ')
n, q = map(int, vals)

queue = Queue()
for i in range(0, n):
    pname, ptime = sys.stdin.readline().rstrip().split(' ')
    queue.enqueue(Process(pname, int(ptime)))

time = 0
while not queue.is_empty():
    p = queue.dequeue()
    if p.time > q:
        p.time -= q
        queue.enqueue(p)
        time += q
    else:
        time += p.time
        print '%s %d' % (p.name, time)