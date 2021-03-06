# atcoder -take a rest-(easy)
#typical greedy
def main():
    N, M = map(int, input().split())
    conflict = [tuple(map(int, input().split())) for i in range(M)]
    newest_destroyed = -1
    conflict.sort(key=lambda x: x[1])
    res = 0
    for l, r in conflict:
        if not (l <= newest_destroyed < r):
            res += 1
            newest_destroyed = r-1
    print(res)
    return


if __name__ == "__main__":
    main()


