import sys

sys.setrecursionlimit(10 ** 7)
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, k = map(int, input().split())

    num = [0] * k
    for i in range(1, n + 1):
        num[i % k] += 1
        
    if k % 2 != 0:
        print(pow(num[0], 3))
    else:
        print(pow(num[0], 3) + pow(num[k // 2], 3))


if __name__ == '__main__':
    resolve()
