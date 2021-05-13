import itertools
import math
import statistics


def main():
    N = int(input())
    city_lst = [list(map(int, input().split())) for _ in range(N)]
    d_lst = [0] * math.factorial(N)

    for i, route in enumerate(itertools.permutations(range(N))):
        for j in range(len(route) - 1):
            d = math.sqrt((city_lst[route[j + 1]][0] - city_lst[route[j]][0])
                          ** 2 + (city_lst[route[j + 1]][1] - city_lst[route[j]][1]) ** 2)
            d_lst[i] += d

    print(f"{statistics.mean(d_lst):.10f}")


if __name__ == "__main__":
    main()
