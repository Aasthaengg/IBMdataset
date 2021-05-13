import sys


def compare(s: str, t: str) -> bool:
    return all(x == y or x == "?" for x, y in zip(s, t))


if __name__ == "__main__":
    S = input()
    T = input()

    len_s = len(S)
    len_t = len(T)

    indexes = []
    for i in range(len_s):
        if i + len_t <= len_s:
            s = S[i : i + len_t]
            if compare(s, T):
                indexes.append(i)

    if len(indexes) == 0:
        print("UNRESTORABLE")
        sys.exit(0)

    decrypted = []
    for j in indexes:

        d = ""
        for i, s in enumerate(S):
            if i in range(j, j + len_t):

                d += T[i - j]
                continue
            if s == "?":
                d += "a"
                continue

            d += s

        decrypted.append(d)
    decrypted.sort()
    print(decrypted[0])