import sys
import bisect

input = sys.stdin.readline

N, Q = map(int, input().split())

STX_array = [list(map(int, input().split())) for _ in range(N)]

STX_array = sorted(STX_array, key=lambda x: x[2])

Q_array = [int(input()) for _ in range(Q)]

index_array = [i for i in range(Q)]

ans_array = [-1] * Q
for STX in STX_array:
    s, t, x = STX
    index_left = bisect.bisect_left(Q_array, s - 0.5 - x)
    index_right = bisect.bisect_left(Q_array, t - 0.5 - x)
    if index_left != index_right:
        now_index = index_left
        while now_index < index_right:
            if index_array[now_index] == now_index:
                ans_array[now_index] = x
                index_array[now_index] = index_right
                now_index += 1
            else:
                old_index = now_index
                now_index = index_array[now_index]
                index_array[old_index] = now_index




for ans in ans_array:
    print(ans)