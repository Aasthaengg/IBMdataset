# AGC029
# A
# Irreversible operation
import itertools

s_list = input()

gr = itertools.groupby(s_list)

num_b = 0
ans = 0

for key,group in gr:
    if key == "B":
        num_b += len(list(group))
    else:
        ans += num_b * len(list(group))
    
print(ans)