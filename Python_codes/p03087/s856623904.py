from typing import List


def query(S: List[str], l: int, r: int) -> int:
    return ac[r - 1] - ac[l - 1]


if __name__ == "__main__":

    N, Q = [int(x) for x in input().split(" ")]
    S = list(input())

    ac = [0]
    count = 0
    for i, s in enumerate(S):
        if i == 0:
            continue

        if S[i - 1] == "A" and S[i] == "C":
            count += 1

        ac.append(count)

    for _ in range(Q):
        l, r = [int(x) for x in input().split(" ")]
        print(query(S, l, r))
