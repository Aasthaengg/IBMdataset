import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    ABC = list(map(int, input().split()))
    print(len(set(ABC)))


if __name__ == '__main__':
    resolve()
