import bisect
import heapq
import sys
import queue


input = sys.stdin.readline
sys.setrecursionlimit(100000)


class V:
    def __init__(self, f):
        self.f = f
        self.v = None

    def __str__(self):
        return str(self.v)

    def ud(self, n):
        if self.v is None:
            self.v = n
        else:
            self.v = self.f(self.v, n)

    def get(self):
        return self.v


def read_values():
    return map(int, input().split())


def read_list():
    return list(read_values())


def main():
    N = int(input())

    left = 0
    right = N - 1
    D = {}
    c = 0
    for _ in range(21):
        if left not in D:
            print(left)
            sys.stdout.flush()
            res = input()
            c += 1
            if res == "Vacant" or c >= 20:
                return

            D[left] = res

        LD = D[left]
        m = (left + right) // 2

        if m not in D:
            print(m)
            sys.stdout.flush()
            res = input()
            c += 1
            if res == "Vacant" and c >= 20:
                return

            D[m] = res

        MD = D[m]

        if (m % 2 == left % 2 and MD == LD) or (m % 2 != left % 2 and MD != LD):
            left = m if left != m else m + 1
        else:
            right = m


if __name__ == "__main__":
    main()
