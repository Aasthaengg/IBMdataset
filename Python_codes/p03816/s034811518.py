from collections import Counter
from functools import reduce

if __name__ == "__main__":
    N = int(input())
    arr = map(int, input().split())

    dic = Counter(arr)
    count = len(dic) - reduce(lambda sum, item: sum + 1, filter(lambda x: x % 2 == 0, dic.values()), 0) % 2
    print(count)
