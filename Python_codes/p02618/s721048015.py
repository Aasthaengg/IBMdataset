
import time

start_time = time.time()

#input
D = int(input())
c_list = list(map(int, input().split()))

s_grid = []
for i in range(D):
    array = list(map(int, input().strip().split(' ')))
    s_grid.append(array)

t_list = [(i%26) for i in range(D)] #task_list

def calculate_score(t_list,score_list,last_grid,change_query_number):
    score_list = score_list[:change_query_number]
    last_grid = last_grid[:change_query_number]

    if len(score_list) > 1:
        score = score_list[change_query_number-1]
        last_list = last_grid[change_query_number-1]
    else:
        score = 0
        last_list = [0 for i in range(26)]

    for d in range(change_query_number,D):
        score += s_grid[d][t_list[d]]
        last_list = [n+1 for n in last_list]
        last_list[t_list[d]] = 0
        for i in range(26):
            score -= c_list[i]*last_list[i]
        score_list.append(score)
        last_grid.append(last_list)
    return score_list, last_grid

#first cal.
previous_s, previous_l = calculate_score(t_list,[],[[0 for i in range(26)]],0)
score = previous_s[-1]

for k in range(1,D):
    X = -1  # k-日目に変える番号を探す
    t_list_loop = t_list
    for i in range(26):  # 26通り試す
        t_list_loop[k] = i
        score_list_k, last_grid_k = calculate_score(t_list_loop, previous_s, previous_l, k)
        if score_list_k[-1] > score:
            X = i
            score = score_list_k[-1]
            score_list_t = score_list_k
            last_grid_t = last_grid_k

    if X != -1:
        t_list[k] = X
        previous_s = score_list_t
        previous_l = last_grid_t

    # print(k,X,score)

    if time.time() - start_time > 1.9:
        break

#final result
for j in range(len(t_list)):
    print(int(t_list[j]) + 1)