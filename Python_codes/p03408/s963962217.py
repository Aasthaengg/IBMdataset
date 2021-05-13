def dict_update(val):
    s = input()
    if s not in v:
        v[s] = val
    else:
        v[s] += val


v = {}
n = int(input())
for i in range(n):
    dict_update(1)
m = int(input())
for j in range(m):
    dict_update(-1)
print(max(max(v.values()), 0))
