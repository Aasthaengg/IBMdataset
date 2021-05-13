from itertools import product
from operator import mul
def main():
    n = int(input())
    f = [tuple(map(int, input().split())) for _ in range(n)]
    p = [tuple(map(int, input().split())) for _ in range(n)]

    patterns = tuple(product([0,1], repeat=10))
    results = []
    for pate in patterns:
        if sum(pate) == 0:
            continue
        r = 0
        for i1, fe in enumerate(f):
            r += p[i1][sum(tuple(map(mul, pate, fe)))]
        results.append(r)
    print(max(results))
if __name__ == '__main__':
    main()