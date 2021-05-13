def main():
    from math import ceil
    n, k = map(int, input().split())
    A = sorted(map(int, input().split()))
    F = sorted(map(int, input().split()))
    A.reverse()
    ok = max(a * f for a, f in zip(A, F))
    ng = -1
    while ok - ng != 1:
        x = (ok + ng) // 2
        cnt = 0
        for a, f in zip(A, F):
            if a * f > x:
                cnt += ceil(a - x / f)
            if cnt > k:
                ng = x
                break
        else:
            ok = x

    print(ok)

if __name__ == "__main__":
    main()