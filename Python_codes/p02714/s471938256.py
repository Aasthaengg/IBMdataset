# D - RGB Triplets
from collections import defaultdict


def main():
    """
    character  A ---- B ---- C
    index     X-dx    X     X+dx
        -> A_index + C_index == 2 * B_index
    """
    _, S = open(0).read().split()
    indices = defaultdict(set)
    for i, c in enumerate(S):
        indices[c].add(i)

    cnt = len(indices["R"]) * len(indices["G"]) * len(indices["B"])
    for x, y, z in ("RGB", "RBG", "BGR"):
        cnt -= sum(
            (i + j) % 2 == 0 and (i + j) // 2 in indices[z]
            for i in indices[x]
            for j in indices[y]
        )
    print(cnt)


if __name__ == "__main__":
    main()
