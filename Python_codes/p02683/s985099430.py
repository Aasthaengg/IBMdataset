import sys
read = sys.stdin.read
readlines = sys.stdin.readlines
from itertools import product
def main():
    n, m, x = map(int, input().split())
    books = []
    for _ in range(n):
        book = tuple(map(int, input().split()))
        books.append(book)
    pro = product((1, 0),repeat=n)
    costs = []

    for proe in pro:
        cost = 0
        algo = [0] * m
        for i1, proee in enumerate(proe):
            if proee:
                cost += books[i1][0]
                for al in range(1, m + 1):
                    algo[al-1] += books[i1][al]
        if all([i >= x for i in algo]):
            costs.append(cost)
    if not costs:
        print(-1)
    else:
        print(min(costs))

if __name__ == '__main__':
    main()
