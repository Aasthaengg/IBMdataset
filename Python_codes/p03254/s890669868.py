import math


def resolve():
    import sys
    input = sys.stdin.readline
    # row = [int(x) for x in input().rstrip().split(" ")]
    # n = int(input().rstrip())
    import heapq  # heapqライブラリのimport
    nx = [int(x) for x in input().rstrip().split(" ")]
    x = nx[1]
    a_list = [int(x) for x in input().rstrip().split(" ")]

    heapq.heapify(a_list)
    ans = 0
    while len(a_list) > 0:
        a = heapq.heappop(a_list)

        if len(a_list) == 0:
            if(x == a):
                ans += 1
            break
        if x >= a:
            ans += 1
            x -= a
        else:
            break


    print(ans)

if __name__ == "__main__":
    resolve()
