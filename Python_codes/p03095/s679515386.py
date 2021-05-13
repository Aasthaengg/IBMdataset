
from collections import Counter
def resolve():
    MOD = 10 ** 9 + 7
    N = int(input())
    S = input()

    CNT = Counter(S)
    ans = 1
    for v in CNT.values():
        ans *= v + 1
        ans %= MOD

    print(ans - 1)


if __name__ == "__main__":
    resolve()
