import heapq
from collections import defaultdict


def main():
    h, w = map(int, input().split())

    d = defaultdict(int)
    for _ in range(h):
        for i in input():
            d[i] -= 1
    char = list(d.values())
    heapq.heapify(char)

    hd, hm = divmod(h, 2)
    wd, wm = divmod(w, 2)
    pair = [-2] * hd + [-1] * hm
    pair = [i * 2 for i in pair]*wd + pair*wm
    heapq.heapify(pair)

    while char:
        tmp = heapq.heappop(char) - heapq.heappop(pair)
        if tmp > 0:
            return "No"
        if tmp == 0:
            continue
        heapq.heappush(char, tmp)
    return "Yes"


if __name__ == "__main__":
    ans = main()
    print(ans)
