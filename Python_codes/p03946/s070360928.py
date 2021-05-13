from collections import defaultdict


def main():
    n, t = map(int, input().split())
    a = list(map(int, input().split()))
    profit = defaultdict(int)
    now_min = a[0]
    for i in range(1, n):
        profit[a[i] - now_min] += 1
        now_min = min(now_min, a[i])
    profit = list(profit.items())
    profit.sort(key=lambda x: x[0], reverse=True)
    print(profit[0][1])


if __name__ == '__main__':
    main()
