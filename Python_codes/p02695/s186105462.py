# -*- coding: utf-8 -*-
from itertools import combinations_with_replacement
def main():
    n, m, q = map(int, input().split())
    xs = []
    for i in range(q):
        xs.append(list(map(int, input().split())))
    max = 0
    for suretu in combinations_with_replacement(range(1, m + 1), n):
        wa = 0
        for x in xs:
            a, b, c, d = x
            if suretu[b - 1] - suretu[a - 1] == c:
                wa += d
        if wa > max:
            max = wa
    print(max)
    

if __name__ == "__main__":
    main()
