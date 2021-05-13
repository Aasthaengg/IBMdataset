import sys
def LI(): return [int(x) for x in sys.stdin.readline().split()]

def main():
    N, K = LI()
    TD = []
    for _ in range(N):
        TD.append(LI())

    TD.sort(key=lambda x: x[1], reverse=True)

    from collections import Counter
    import heapq

    counter = Counter()
    S = TD[:K]
    TD = TD[K:]
    queue = []
    for t, d in S:
        counter[t] += 1
        heapq.heappush(queue, (d, t))

    sum_ = sum([i[1] for i in S])
    maximum = sum_ + len(counter)**2
    while len(queue) > 0:
        d, t = heapq.heappop(queue)
        if counter[t] == 1:
            continue
        counter[t] -= 1
        sum_ -= d
        while len(TD) > 0:
            new_t, new_d = TD.pop(0)
            if counter[new_t] == 0:
                counter[new_t] += 1
                sum_ += new_d
                maximum = max(maximum, sum_ + len(counter)**2)
                break

    print(maximum)


main()