import sys
input = sys.stdin.readline
# sys.setrecursionlimit(100000)


def main():
    n = int(input().strip())
    timetable = []
    profites = []
    ans = -(10**9)

    for _ in range(n):
        timetable.append([int(i) for i in input().strip().split()])
    for _ in range(n):
        profites.append([int(i) for i in input().strip().split()])

    for i in range(1, 2**10):
        on_service = [0] * 10
        overlaps = [0] * n
        for j in range(10):
            if i >> j & 1:
                on_service[j] = 1
                for k, table in enumerate(timetable):
                    if table[j] == 1:
                        overlaps[k] += 1
        _tmp = 0
        for m in range(n):
            ptr = overlaps[m]
            _tmp += profites[m][ptr]
        ans = max(ans, _tmp)
    print(ans)
    return


if __name__ == "__main__":
    main()
