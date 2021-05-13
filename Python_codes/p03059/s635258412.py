import sys
from bisect import insort_left
def input(): return sys.stdin.readline().strip()


def main():
    A, B, T = map(int, input().split())
    print(T // A * B)



if __name__ == "__main__":
    main()
