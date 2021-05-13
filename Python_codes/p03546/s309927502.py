from itertools import permutations
from collections import Counter

def main():
    H, W = map(int, input().split())
    cost = [[0]*10 for _ in range(10)]

    for i in range(10):
        line = tuple(map(int, input().split()))
        for j, e in enumerate(line):
            cost[i][j] = e

    seq = (0, 2, 3, 4, 5, 6, 7, 8, 9)
    for i in range(2, 10):
        for p in permutations(seq, i):
            temp = sum([cost[p[j]][p[j+1]] for j in range(i-1)])
            temp += cost[p[-1]][1]
            cost[p[0]][1] = min(cost[p[0]][1], temp)

    c = Counter()
    for _ in range(H):
        temp = Counter(tuple(map(int, input().split())))
        c += temp

    ans = 0
    for i in seq:
        ans += c[i] * cost[i][1]
    print(ans)

if __name__ == "__main__":
    main()