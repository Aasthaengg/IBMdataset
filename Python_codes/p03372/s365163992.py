def main():

    N, C = map(int, input().split())
    A = []
    for _ in range(N):
        x, v = map(int, input().split())
        A.append([x, v])

    clock = [0]
    clock_r = [0]
    v = 0
    for i in range(N):
        v += A[i][1]
        clock.append(v-A[i][0])
        clock_r.append(v-2*A[i][0])
    prefix_clock = [0]
    prefix_clock_r = [0]
    for i in range(1, N+1):
        prefix_clock.append(max(prefix_clock[-1], clock[i]))
        prefix_clock_r.append(max(prefix_clock_r[-1], clock_r[i]))

    cclock = [0]
    cclock_r = [0]
    v = 0
    for i in range(N):
        v += A[N-1-i][1]
        cclock.append(v-(C-A[N-1-i][0]))
        cclock_r.append(v-2*(C-A[N-1-i][0]))
    prefix_cclock = [0]
    prefix_cclock_r = [0]
    for i in range(1, N+1):
        prefix_cclock.append(max(prefix_cclock[-1], cclock[i]))
        prefix_cclock_r.append(max(prefix_cclock_r[-1], cclock_r[i]))

    # print(A, C)
    # print(prefix_clock)
    # print(prefix_cclock)

    max_v = float('-inf')
    for i in range(N+1):
        v1 = prefix_clock_r[i]
        v2 = prefix_cclock[N-i]
        max_v = max(max_v, v1+v2)
        v3 = prefix_clock[i]
        v4 = prefix_cclock_r[N-i]
        max_v = max(max_v, v3+v4)
    return max_v


if __name__ == '__main__':
    print(main())