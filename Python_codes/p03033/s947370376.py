from bisect import bisect_left

N,Q = (int(x) for x in input().split())

stop_arr = [tuple(map(int, input().split())) for _ in range(N)]
Q_arr = [int(input()) for _ in range(Q)]

stop_arr.sort(key=lambda x:x[2])

ans_arr = [-1]*Q
skip_arr = [-1]*(Q+1)

for s,t,x in stop_arr:
    q_start = bisect_left(Q_arr, s-x)
    q_stop = bisect_left(Q_arr, t-x)
    l = q_start
    while l < q_stop:
        if skip_arr[l] == -1:
            skip_arr[l] = q_stop
            ans_arr[l] = x
            l += 1
        else:
            l = skip_arr[l]

print(*ans_arr, sep="\n")
