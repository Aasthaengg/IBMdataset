def main():
    N, C, K = list(map(int, input().split()))
    T = [int(input()) for _ in range(N)]
    # 到着時刻が遅い人から貪欲に拾っていく
    T.sort(reverse=True)
    arrival_time_from = T[0] - K
    cnt_bus, cnt_passenger = 1, 0
    for t in T:
        if t >= arrival_time_from and cnt_passenger < C:
            cnt_passenger += 1
        else:
            arrival_time_from = t - K
            cnt_passenger = 1
            cnt_bus += 1
    print(cnt_bus)


if __name__ == '__main__':
    main()