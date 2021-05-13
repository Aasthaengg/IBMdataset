import heapq

def solve():
    N, T = tuple(map(int, input().split()))
    AS = tuple(map(int, input().split()))

    # print(N, T)
    # print(AS)

    lis = []
    D = {}

    m = -float('inf')
    c = 0
    for i in range(len(AS) - 1, -1, -1):
        x = AS[i]
        heapq.heappush(lis, -x)
        D[i] = -lis[0]

    for i in range(len(AS)):
        x = AS[i]

        d = D[i] - AS[i]
        if d > 0:
            if m < d:
                m = d
                c = 1
            elif m == d:  # max と同じ値なら counter を ++
                c += 1

    return c


if __name__ == '__main__':
    res = solve()
    print(res)
