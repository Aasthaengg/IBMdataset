import copy

n = int(input())
t = list(map(int, input().split()))
m = int(input())
dorink = [list(map(int, input().split())) for _ in range(m)]
for i in range(m):
    t_copy = copy.deepcopy(t)
    t_copy[dorink[i][0] - 1] = dorink[i][1]
    print(sum(t_copy))
