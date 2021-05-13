import sys
import bisect
from collections import deque
input = lambda: sys.stdin.readline().rstrip()


def solve():
    s = list(map(lambda x: ord(x) - ord('a'), input()))
    t = list(map(lambda x: ord(x) - ord('a'), input()))
    n = len(s)
    a_list = [[] for _ in range(26)]

    for i in range(n):
        a_list[s[i]].append(i)

    for tt in list(set(t)):
        if len(a_list[tt]) == 0:
            print(-1)
            exit()

    now_i = -1
    count = 0
    t = deque(t)
    ts = t.popleft()
    while True:
        index = bisect.bisect_right(a_list[ts], now_i)
        if index == len(a_list[ts]):
            count += 1
            now_i = -1
        else:
            now_i = a_list[ts][index]
            if not t:
                break
            ts = t.popleft()

    print(n * count + now_i + 1)


if __name__ == '__main__':
    solve()
