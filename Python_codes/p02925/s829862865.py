import sys
input = sys.stdin.readline
N = int(input())
A_array = [list(map(int, input().split())) for _ in range(N)]

# print(A_array)

s_index = [0] * N

ans_date = 1
finish_player = 0
match_count = 0
M = N * (N-1) // 2
first_flag = 1
while(1):
    flag = 0
    match_array = [0] * N
    if first_flag:
        match_candidate = [i for i in range(N)]
        first_flag = 0
    next_match = []
    for i in match_candidate:
        if match_array[i] == 1 or s_index[i] == N - 1:
            continue
        vs = A_array[i][s_index[i]] - 1
        # print(i,vs)
        if match_array[vs] != 1 and A_array[vs][s_index[vs]] - 1 == i:
            match_count += 1
            match_array[i] = 1
            s_index[i] += 1
            match_array[vs] = 1
            s_index[vs] += 1
            flag = 1
            next_match.append(i)
            next_match.append(vs)
    if flag == 0:
        print(-1)
        exit()
    if match_count == M:
        break
    ans_date += 1
    match_candidate = next_match
print(ans_date)
