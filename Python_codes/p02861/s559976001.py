# row = [int(x) for x in input().rstrip().split(" ")]
# n = int(input().rstrip())
# s = input().rstrip()
# row = [int(input().rstrip()) for _ in range(n)]

def resolve():
    import sys
    input = sys.stdin.readline
    n = int(input().rstrip())

    cities = [[int(x) for x in input().rstrip().split(" ")] for _ in range(n)]
    import math

    import itertools

    length_list = []
    p = itertools.permutations(list(range(n)), n)
    for v in p:
        length = 0
        for city_i in range(n - 1):
            city1 = cities[v[city_i]]
            city2 = cities[v[city_i + 1]]
            length += math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

        length_list.append(length)

    print(sum(length_list) / len(length_list))


if __name__ == "__main__":
    resolve()
