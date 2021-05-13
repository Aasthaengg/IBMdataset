import heapq as hq
import sys


def main():
    input = sys.stdin.buffer.readline
    x, y, a, b, c = map(int, input().split())
    p = list(map(int, input().split()))
    q = list(map(int, input().split()))
    r = list(map(int, input().split()))
    p = sorted(p, reverse=True)[:x]
    q = sorted(q, reverse=True)[:y]
    r.sort(reverse=True)
    hq.heapify(p)
    hq.heapify(q)
    # r_pointer以降のリンゴは無色
    r_pointer = 0
    while True:
        red_min = p[0]
        green_min = q[0]
        if red_min < green_min and red_min < r[r_pointer]:
            hq.heappop(p)
            hq.heappush(p, r[r_pointer])
            r_pointer += 1
            if r_pointer >= c:
                break
        elif red_min >= green_min and green_min < r[r_pointer]:
            hq.heappop(q)
            hq.heappush(q, r[r_pointer])
            r_pointer += 1
            if r_pointer >= c:
                break
        else:
            break
    print(sum(p) + sum(q))


if __name__ == "__main__":
    main()
