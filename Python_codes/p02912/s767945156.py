from heapq import heappush as hpush
from heapq import heappop as hpop

class Descending_HeapQueue:
    def __init__(self, hq=[]):
        self.hq = []
        for i in hq:
            self.push(i)
    def push(self, n):
        hpush(self.hq, -n)
    def pop(self):
        return -hpop(self.hq)
    def sum(self):
        return -sum(self.hq)
    def __str__(self):
        return [-i for i in self.hq].__str__()

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    dhq = Descending_HeapQueue(A)
    for _ in range(M):
        dhq.push(dhq.pop() // 2)
    print(dhq.sum())
main()