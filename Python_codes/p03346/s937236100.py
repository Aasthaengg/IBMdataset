N = int(input())
P = [int(input()) for _ in range(N)]
permu_index = {}
for i in range(N):
    permu_index[P[i]] = i
ans = []
for i in range(1, N+1):
    ans.append(permu_index[i])
max_len = 0
tmp = 1
now = ans[0]
for a in ans[1:]:
    if a > now:
        tmp += 1
        now = a
    else:
        max_len = max(max_len, tmp)
        now = a
        tmp = 1
max_len = max(max_len, tmp)
print(N-max_len)
