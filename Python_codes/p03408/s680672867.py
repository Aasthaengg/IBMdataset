import collections

n = int(input())
s = [input() for _ in range(n)]
m = int(input())
t = [input() for _ in range(m)]

s_counter = collections.Counter(s)
t_counter = collections.Counter(t)
t_keys = list(t_counter.keys())
ans = []

for key in s_counter.keys():
    if key in t_keys:
        ans.append(int(s_counter[key]) - int(t_counter[key]))
    else:
        ans.append(s_counter[key])
max_ans = max(ans)
if max_ans < 0:
    print(0)
else:
    print(max_ans)
