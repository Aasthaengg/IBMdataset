import sys

input = sys.stdin.readline


def main():
    N = int(input())

    # Initialize
    l, r = 0, N - 1
    print(l, flush=True)
    sl = input().rstrip()
    print(r, flush=True)
    sr = input().rstrip()
    if sl == "Vacant" or sr == "Vacant":
        exit()

    for _ in range(18):
        mid = (l + r) // 2
        print(mid, flush=True)
        s = input().rstrip()
        if s == "Vacant":
            exit()
        if (mid - l) % 2 == 0:
            if sl == s:
                l = mid
                sl = s
            else:
                r = mid
                sr = s
        else:
            if sl == s:
                r = mid
                sr = s
            else:
                l = mid
                sl = s


if __name__ == "__main__":
    main()
