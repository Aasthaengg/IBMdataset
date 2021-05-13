#damedatta..
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ms = 0
    ps = 0
    mr = 0
    pr = 0
    for i, v in enumerate(a):
        if i % 2:
            if ms + v < 0:
                ms += v
            else:
                mr += abs(-1 - ms - v)
                ms = -1
            if ps + v > 0:
                ps += v
            else:
                pr += abs(1-ps-v)
                ps = 1
        else:
            if ms + v > 0:
                ms += v
            else:
                mr += abs(1-ms-v)
                ms = 1
            if ps + v < 0:
                ps += v
            else:
                pr += abs(-1-ps-v)
                ps = -1
    return min(mr, pr)
print(main())
