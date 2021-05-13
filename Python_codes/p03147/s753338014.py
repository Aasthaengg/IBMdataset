def solve():
    n = int(input())
    h = list(map(int, input().split()))
    print(watering(h))


def watering(h):
    if 0 in h:
        x = h.index(0)
        return watering(h[:x]) + watering(h[x + 1:])
    if h:
        if max(h) == 1:
            return 1
        else:
            h = list(map(lambda x: x - 1, h))
            return watering(h) + 1
    return 0



if __name__ == '__main__':
    solve()
