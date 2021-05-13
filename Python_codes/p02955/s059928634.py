
import sys
import math
INF = 1 << 20

def main():
    N, K = [int(i) for i in sys.stdin.readline().strip().split()]
    numbers = [int(i) for i in sys.stdin.readline().strip().split()]
    print("%d" % solve(N, K, numbers))


def solve(N, K, numbers):

    total = sum(numbers)
    ans = 1
    candidates = []
    
    divisor = 1
    # list all possible divisors
    while divisor * divisor <= total:
        if total % divisor == 0:
            candidates.append(divisor)
            candidates.append(total/divisor)
        divisor += 1
    candidates = sorted(candidates, reverse=True)

    for divisor in candidates:
        mods = []
        for number in numbers:
            mods.append(number % divisor)
        mods.sort()
        A = sum(mods)

        need = INF
        index = math.floor(-1 * A/divisor)
        need = sum(mods[0:index])
        if need <= K:
            ans = max(ans, divisor)

    return ans


if __name__ == "__main__":
    main()