def main(n, m, h, roads):
    is_good_peaks = [True] * n
    for road in roads:
        a, b = road[0] - 1, road[1] - 1
        if h[a] <= h[b]:
            is_good_peaks[a] = False
        if h[b] <= h[a]:
            is_good_peaks[b] = False
    print(sum(is_good_peaks))


if __name__ == "__main__":
    n, m = map(int, input().split())
    h = tuple(map(int, input().split()))
    roads = []
    for _ in range(m):
        roads.append(tuple(map(int, input().split())))
    main(n, m, h, roads)
