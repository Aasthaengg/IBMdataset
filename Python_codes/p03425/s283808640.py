from itertools import combinations as comb
from collections import Counter


def main():
    n = int(input())
    ss = [input()[0] for _ in range(n)]
    marchs = ['M', 'A', 'R', 'C', 'H']
    ssc = Counter(ss)

    Counts = []
    for march in marchs:
        if march in ssc:
            Counts.append(ssc[march])

    ans = 0
    for a, b, c in comb(Counts, 3):
        ans += a*b*c
    print(ans)


if __name__ == "__main__":
    main()
