import sys
input = sys.stdin.readline
import bisect

N,Q = (int(x) for x in input().split())

stop_arr = [tuple(map(int, input().split())) for _ in range(N)]
Q_arr = [int(input()) for _ in range(Q)]

stop_arr_ind = list(range(N))
stop_arr_ind.sort(key=lambda x:stop_arr[x][2])

ans_arr = [-1]*Q
skip_arr = [-1]*(Q+1)

def update_skip(skip_arr, x):
    if skip_arr[x] == -1:
        return x
    x_dest = update_skip(skip_arr, skip_arr[x])
    skip_arr[x] = x_dest
    return x_dest

for i in stop_arr_ind:
    s,t,x = stop_arr[i]
    q_start = bisect.bisect_left(Q_arr, s-x)
    q_stop = bisect.bisect_left(Q_arr, t-x)
    l = q_start
    while l < q_stop:
        if skip_arr[l] == -1:
            skip_arr[l] = q_stop
            ans_arr[l] = x
            l += 1
        else:
            l = update_skip(skip_arr, l)

print(*ans_arr, sep="\n")
