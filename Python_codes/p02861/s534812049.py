from itertools import permutations

n = int(input())
t = [list(map(int, input().split())) for _ in range(n)]

perms = permutations(list(range(n)))
ans = 0
length = 0
for perm in perms:
    length += 1
    cur_i = 0
    tmp = 0
    for i in range(1, n):
        x = t[perm[cur_i]][0] - t[perm[i]][0]
        x = x**2
        y = t[perm[cur_i]][1] - t[perm[i]][1]
        y = y**2
        tmp += (x + y)**0.5
        cur_i = i
    ans += tmp
print(ans / length)
