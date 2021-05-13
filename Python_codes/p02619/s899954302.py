#input
D = int(input())
c_list = list(map(int, input().split()))

s_grid = []
for i in range(D):
    array = list(map(int, input().strip().split(' ')))
    s_grid.append(array)

t_list = [int(input()) -1 for i in range(D)]
last_list = [0 for i in range(26)]

def calculate_score(last_list):
    score = 0
    for d in range(D):
        score += s_grid[d][t_list[d]]
        last_list = [n+1 for n in last_list]
        last_list[t_list[d]] = 0
        for i in range(26):
            score -= c_list[i]*last_list[i]
        print(score)


calculate_score(last_list)