import heapq
class HeapQ:
    def __init__(self, L, desc=False):
        if desc:
            L = [-l for l in L]
        self.sign = -1 if desc else 1
        self.HQ = L
        heapq.heapify(self.HQ)
    def pop(self):
        return heapq.heappop(self.HQ) * self.sign
    def push(self, x):
        heapq.heappush(self.HQ, x * self.sign)
    def get_list(self):
        return list([-hq for hq in self.HQ]) if self.sign == -1 else list(self.HQ)

n, m = map(int, input().split())
A = list(map(int, input().split()))
hq = HeapQ(A, desc=True)
for _ in range(m):
    hq.push(hq.pop() // 2)

print(sum(hq.get_list()))