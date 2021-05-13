N = int(input())
a = list(map(int, input().split(' ')))
a.sort(reverse=True)

process = []
p_seed = a.pop(0)
n_seed = a.pop(-1)
for e in a:
    if e >= 0:
        process.append((n_seed, e))
        n_seed -= e
    else:
        process.append((p_seed, e))
        p_seed -= e
process.append((p_seed, n_seed))
m = p_seed - n_seed
print(m)
for x, y in process:
    print(str(x) + ' ' + str(y))
