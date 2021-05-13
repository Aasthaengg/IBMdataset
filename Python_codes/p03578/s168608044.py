from collections import defaultdict
n = int(input())
d_ls = list(map(int, input().split()))
m = int(input())
t_ls = list(map(int, input().split()))

have_dict = defaultdict(int)
must_dict = defaultdict(int)
for i in range(n):
    have_dict[d_ls[i]] += 1
for i in range(m):
    must_dict[t_ls[i]] += 1
ans = 'YES'
for i in range(m):
    if must_dict[t_ls[i]] > have_dict[t_ls[i]]:
        ans = 'NO'
print(ans)

