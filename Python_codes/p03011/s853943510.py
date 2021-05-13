from itertools import permutations

# input
P, Q, R = map(int, input().split())

t = {
    "A": {
        "B": P,
        "C": R
    },
    "B": {
        "A": P,
        "C": Q
    },
    "C": {
        "A": R,
        "B": Q
    }
}
# check
P = list(permutations(["A", "B", "C"], 3))
T = [sum([t[p[i]][p[i + 1]]for i in range(0, 2)]) for p in P]

print(min(T))