def ask(n):
    # global test
    l = ["Vacant", "Male", "Female"]
    # if test is not None:
    #     return l.index(test[n])
    # else:
    print(n, flush=True)
    return l.index(input())


def resolve():
    N = int(input())
    sheets = [-1 for _ in range(N)]
    sheets[0] = ask(0)
    if sheets[0] == 0:
        return
    sheets[N - 1] = ask(N - 1)
    if sheets[N - 1] == 0:
        return
    ng = 0
    ok = N - 1
    mid = (ok + ng) // 2
    sheets[mid] = ask(mid)
    # cnt = 3
    while sheets[mid] != 0:  # and cnt < 30:
        mid = (ok + ng) // 2
        sheets[mid] = ask(mid)
        # cnt += 1
        # print(mid, file=sys.stderr)
        if ((mid - ng) % 2 and sheets[ng] == sheets[mid]) \
                or ((mid - ng + 1) % 2 and sheets[ng] != sheets[mid]):
            ok = mid
        else:
            ng = mid
    # if cnt > 20:
    #     raise SystemError("cnt")
    # else:
    #     print("cnt=", cnt, file=sys.stderr)


resolve()
