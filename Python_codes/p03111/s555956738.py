from itertools import product
from sys import stdin
input = stdin.buffer.readline

def main():
    n, *abc = map(int, input().split())
    l = [int(input()) for _ in range(n)]

    ans = 10**9
    for prod in product([0, 1, 2, 3], repeat=n):
        cost = 10 * (n-3)
        lengths = [0, 0, 0]
        for i, x in enumerate(prod):
            if x < 3:
                lengths[x] += l[i]
            else:
                cost -= 10

        for i in lengths:
            if i == 0:
                break

        else:
            for i, x in enumerate(abc):
                cost += abs(x - lengths[i])
            if cost < ans:
                ans = cost

    print(ans)

main()