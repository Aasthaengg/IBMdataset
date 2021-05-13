from collections import defaultdict as dd
from functools import reduce

if __name__ == "__main__":
    N = int(input())
    arr = map(int, input().split())

    dic = dd(int)

    for el in arr:
        dic[el] += 1

    count = len(dic) - len(list(filter(lambda x: x %
                                       2 == 0, dic.values()))) % 2
    print(count)
