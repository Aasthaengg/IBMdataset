import numpy as np


def parse():
    n, k = map(int, input().split())
    p = list(map(int, input().split()))
    c = list(map(int, input().split()))
    pc = {i: (pi - 1, ci) for i, (pi, ci) in enumerate(zip(p, c))}
    return k, pc


def split_simple():
    k, pc = parse()
    lst = [[]]
    lst[0].append(pc.pop(0))
    while True:
        if not pc:
            break
        p, _ = lst[-1][-1]
        if p in pc:
            pcj = pc.pop(p)
            lst[-1].append(pcj)
        else:
            j = next(iter(pc.keys()))
            pcj = pc.pop(j)
            lst.append([pcj])
    return k, [np.array([ls[1] for ls in lst_], dtype=np.long) for lst_ in lst]


def inner(n, k, s, sim):
    # print(sim)
    # print(s)
    if sim.shape[1] == 1:
        return sim.max()
    if k < n or s <= 0:
        return sim.max()
    div = k // n
    mod = k % n
    # print(k, n, div, mod)
    if mod == 0:
        return max(s * div, s * (div - 1) + sim.max())
    try:
        return max(s * div + sim[:, :mod].max(), s * (div - 1) + sim[:, :mod].max())
    except ValueError:
        print(mod)
        print(sim)
        print(sim.shape)
        raise


def main():
    k, data_set = split_simple()
    result = min([d.min() for d in data_set])
    for data in data_set:
        n = data.size
        rep = np.repeat(data[None], 2, axis=0).flatten()
        # sim_ = np.array([[rep[i:i+p].sum()
        #                  for p in range(1, min(k, n) + 1)] for i in range(n)])
        sim = np.array([np.cumsum(rep[i:i+min(k, n)]) for i in range(n)])
        # print((sim == sim_).all())
        cand = inner(n, k, data.sum(), sim)
        result = max(result, cand)
    print(result)


if __name__ == "__main__":
    main()
