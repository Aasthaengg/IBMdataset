import heapq


def main():
    X, Y, A, B, C = list(map(int, input().split(' ')))
    P = list(map(int, input().split(' ')))
    Q = list(map(int, input().split(' ')))
    R = list(map(int, input().split(' ')))
    P.sort(reverse=True)
    Q.sort(reverse=True)
    R.sort(reverse=True)
    que = []
    for p in P[:X]:
        heapq.heappush(que, p)
    for q in Q[:Y]:
        heapq.heappush(que, q)
    for r in R:
        min_que = heapq.heappop(que)
        if min_que >= r:
            heapq.heappush(que, min_que)
            break
        else:
            heapq.heappush(que, r)
    print(sum(que))


if __name__ == '__main__':
    main()
