import sys
input = sys.stdin.readline


def check(T, usable: set):
    for t in T:
        if t not in usable:
            return 0
    return len(T)


def main():
    S = input().rstrip("\n")
    usable = {"A", "C", "G", "T"}
    candidates = []
    for i in range(len(S)):
        for j in range(i, len(S)):
            T = S[i:j+1]
            res = check(T, usable)
            candidates.append(res)

    print(max(candidates))


if __name__ == "__main__":
    main()
