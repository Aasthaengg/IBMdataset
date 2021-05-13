import math
import itertools

def main():
    N = int(input())
    towns = []
    for _ in range(N):
        x, y = map(int, input().split())
        towns.append([x, y])

    ans = 0
    for order in itertools.permutations(list(range(N)), N):
        d = 0
        for i in range(N-1):
            s, e = order[i], order[i+1]
            d += math.sqrt((towns[s][0] - towns[e][0]) ** 2 + (towns[s][1] - towns[e][1]) ** 2)
        ans += d / math.factorial(N)
    print(ans)


if __name__ == '__main__':
    main()
