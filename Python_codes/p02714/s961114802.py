# D - RGB Triplets
from collections import defaultdict


def main():
    _, S = open(0).read().split()
    indices, doubled_indices = defaultdict(list), defaultdict(set)
    for i, c in enumerate(S):
        indices[c].append(i)
        doubled_indices[c].add(2 * i)

    cnt = len(indices["R"]) * len(indices["G"]) * len(indices["B"])
    for x, y, z in ("RGB", "RBG", "BGR"):
        cnt -= sum(i + j in doubled_indices[z] for i in indices[x] for j in indices[y])
    print(cnt)


if __name__ == "__main__":
    main()
