import sys
import heapq


def input():
    return sys.stdin.readline().strip()


MOD = 10 ** 9 + 7
sys.setrecursionlimit(20000000)


def main():
    X, Y, A, B, C = map(int, input().split())
    red = list(map(int, input().split()))
    green = list(map(int, input().split()))
    nocolor = list(map(int, input().split()))

    red.sort()
    green.sort()
    nocolor.sort()
    answer = sum(red[A - X :]) + sum(green[B - Y :])
    heap = red[A - X :] + green[B - Y :]
    heapq.heapify(heap)
    flag = 0
    while heap and flag < C:
        m = heapq.heappop(heap)
        if nocolor[flag] > m:
            answer -= m
            answer += nocolor[flag]
            heapq.heappush(heap, nocolor[flag])
            flag += 1
        else:
            heapq.heappush(heap, m)
            flag += 1

    print(answer)


if __name__ == "__main__":
    main()
