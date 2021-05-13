import string

s = input()
alps = string.ascii_lowercase
mx = {c:0 for c in alps}
tmp = {c:0 for c in alps}

for char in s:
    for alp in alps:
        if alp == char:
            mx[alp] = max(mx[alp], tmp[alp])
            tmp[alp] = 0
        else:
            tmp[alp] += 1

for alp in alps:
    mx[alp] = max(mx[alp], tmp[alp])

print(min(mx.values()))