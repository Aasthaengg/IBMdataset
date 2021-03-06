def main():
    N, C = list(map(int, input().split(' ')))
    progams = [list(map(int, input().split(' '))) for _ in range(N)]
    progams.sort(key=lambda p: p[0])  # sort in ascending order of start time
    recorders = [[0, 0] for _ in range(C)]  # (end time, channel)
    for prog in progams:
        s, t, c = prog
        for i in range(C):
            can_record = (c == recorders[i][1] and recorders[i][0] <= s) or \
                (c != recorders[i][1] and recorders[i][0] < s)
            if can_record:
                recorders[i][0] = t
                recorders[i][1] = c
                break
    ans = 0
    for i in range(C):
        if recorders[i][0] > 0:
            ans += 1
    print(ans)


if __name__ == '__main__':
    main()