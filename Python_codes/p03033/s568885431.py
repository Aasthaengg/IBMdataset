from collections import Counter, defaultdict
import sys
sys.setrecursionlimit(10 ** 5 + 10)
input = sys.stdin.readline
from math import factorial
import heapq, bisect
import math

def main():
    kouji_num, person_num = map(int, input().split())
    koji_data = [list(map(int, input().split())) for i in range(kouji_num)]
    person_data = [int(input()) for i in range(person_num)]

    event_list = [0 for i in range(kouji_num * 2)]
    now_kouji = set()

    for i in range(kouji_num):
        start, fin, position = koji_data[i]
        event_list[2 * i] = (start - position - 0.25, 1, position)
        event_list[2 * i + 1] = (fin - position - 0.75, 0, position)
    event_list.sort(key=lambda x: x[0])

    ans = 10 ** 9 + 1
    now_ind = 0
    for i in range(person_num):
        person_start = person_data[i]
        while now_ind < kouji_num * 2:
            time_data, flg, position = event_list[now_ind]
            if time_data > person_start:
                break

            if flg:
                now_kouji.add(position)
                ans = min(ans, position)
            else:
                now_kouji.remove(position)
                if len(now_kouji) == 0:
                    ans = 10 ** 9 + 1
                elif ans == position:
                    ans = min(now_kouji)

            now_ind += 1
        if ans == 10 ** 9 + 1:
            print(-1)
        else:
            print(ans)





if __name__ == '__main__':
    main()

