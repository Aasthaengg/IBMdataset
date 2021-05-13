from itertools import permutations
n = int(input())
point_ls = [0] * n
for i in range(n):
    point_ls[i] = list(map(int, input().split()))
ind_ls = [i for i in range(n)]
diff_ls = []
for start, end in permutations(ind_ls, 2):
    diff = [0] * 2
    diff[0] = point_ls[end][0] - point_ls[start][0]
    diff[1] = point_ls[end][1] - point_ls[start][1]
    diff_ls.append(diff)
ans = 0
for diff in diff_ls:
    same = 0
    for diff2 in diff_ls:
        if diff == diff2:
            same += 1
    ans = max(ans, same)
print(n-ans)
    



