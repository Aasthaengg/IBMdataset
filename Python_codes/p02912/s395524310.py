# 解説を読んだ。優先度付きキューね，はい。
import heapq


def main():
    item_no, discount_no = [int(x) for x in input().split()]
    prices = [int(x) * -1 for x in input().split()]
    heapq.heapify(prices)

    for _ in range(discount_no):
        current_max = heapq.heappop(prices)
        current_max = current_max * -1 // 2 * -1
        heapq.heappush(prices, current_max)

    print(- sum(prices))


if __name__ == '__main__':
    main()
