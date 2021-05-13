from heapq import heapify, heappop
from sys import stdin
def input():
    return stdin.readline().strip()

def main():
    n, k = map(int, input().split())

    dt = [(0, 0)] * n
    for i in range(n):
        t, d = map(int, input().split())
        dt[i] = (d, t-1)

    dt.sort(key=lambda x: x[0], reverse=True)

    # select k biggest points
    base = 0
    variety = [0] * n
    bonus = 0
    heap = []
    for d, t in dt[:k]:
        base += d
        if variety[t] == 0:
            bonus += 1
        variety[t] += 1
        heap.append((d, t))
    heapify(heap)

    # select exchange candidates
    new_dt = []
    for d, t in dt[k:]:
        if variety[t] == 0:
            variety[t] = 1
            new_dt.append((d, t))

    # exchange
    ans = base + bonus * bonus
    for new_d, new_t in new_dt:
        d, t = heappop(heap)
        while len(heap) > 0 and variety[t] == 1:
            d, t = heappop(heap)
        if len(heap) == 0:
            break
        variety[t] -= 1

        base -= d - new_d
        bonus += 1
        if ans < base + bonus * bonus:
            ans = base + bonus * bonus

    print(ans)

main()