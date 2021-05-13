from typing import List


def changes(amount: int, kind: int, coins: List[int]) -> int:

    T: List[int] = [50001] * (amount + 1)
    T[0] = 0

    for i in range(kind):
        for j in range(coins[i], amount + 1):
            T[j] = min(T[j], T[j - coins[i]] + 1)

    return T[amount]


def main() -> None:
    n, m = [int(x) for x in input().split()]
    c = [int(x) for x in input().split()]

    print(changes(n, m, c))


main()

