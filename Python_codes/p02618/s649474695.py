import time
import copy

start_time = time.time()

#input
D = int(input())
c_list = list(map(int, input().split()))

s_grid = []
for i in range(D):
    array = list(map(int, input().strip().split(' ')))
    s_grid.append(array)

t_list = [(i%26) for i in range(D)] #task_list

def calculate_score(query_list,previous_score,last_list,F):
    score = previous_score
    for d in range(F,F+1):
        score += s_grid[d][query_list[d]]
        last_list = [n+1 for n in last_list]
        last_list[query_list[d]] = 0
        for i in range(26):
            score -= c_list[i]*last_list[i]
    return score , last_list

score = 0
last_list = [0 for i in range(26)]

for k in range(0,D):
    X = -1  # k-日目に変える番号を探す
    t_list_loop = copy.deepcopy(t_list)
    p = 0
    for i in range(26):  # 26通り試す
        t_list_loop[k] = i
        score_k, last_list_k = calculate_score(t_list_loop,score,last_list,k)
        if score_k > p:
            X = i
            p = score_k
            m = last_list_k
        #print(t_list_loop,i,X,p,score_k)

    if X != -1:
        #最大のXを投入
        t_list[k] = X
        score = p
        last_list = m
    else:
        score = p
        last_list = m

    if time.time() - start_time > 1.9:
        break

for j in range(len(t_list)):
    print(int(t_list[j]) + 1)