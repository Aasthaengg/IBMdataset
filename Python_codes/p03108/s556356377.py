n, m = map(int, input().split())
list_ab = []
for _ in range(m):
    a, b = map(int, input().split())
    list_ab.append((a - 1, b - 1))


# Unionfind
_group = {i: i for i in range(n)}
_size = {i: 1 for i in range(n)}


def group(i):
    vertices = []
    while _group[i] != i:
        vertices.append(i)
        i = _group[i]
    for v in vertices:
        _group[v] = i
    return i


def size(i):
    return _size[group(i)]


convenience = [0]

for a, b in list_ab[::-1]:
    ga, gb = group(a), group(b)

    if ga != gb:
        convenience.append(convenience[-1] + size(ga) * size(gb))
        if ga < gb:
            _group[group(b)] = ga

            _size[ga] += _size[gb]
        else:
            _group[group(a)] = gb
            _size[gb] += _size[ga]
    else:
        convenience.append(convenience[-1])


convenience.reverse()
inconvenience = [n * (n - 1) // 2 - c for c in convenience[1:]]


for i in inconvenience:
    print(i)
