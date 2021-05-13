def abc171d_replacing():
    n = int(input())
    a = list(map(int, input().split()))
    a_dict = {}
    for v in a:
        if a_dict.get(v) is None:
            a_dict[v] = 1
        else:
            a_dict[v] += 1
    q = int(input())
    s = []
    total = 0
    for k, v in a_dict.items():
        total += k * v
    for _ in range(q):
        b, c = map(int, input().split())
        if b in a_dict.keys():
            total += (c * a_dict[b] - b * a_dict[b])
            if c in a_dict.keys():
                a_dict[c] += a_dict[b]
            else:
                a_dict[c] = a_dict[b]
            del a_dict[b]
        s.append(total)

    for v in s:
        print(v)


abc171d_replacing()