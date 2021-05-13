import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n = int(input())
    AB = [list(map(int, input().split())) for _ in range(n)]
    for i in range(n):
        a, b = AB[i]
        AB[i] = [a + b, a, b]
    AB.sort(key=lambda x: x[0], reverse=True)

    score_t = sum(AB[i][1] for i in range(n) if i % 2 == 0)
    score_a = sum(AB[i][2] for i in range(n) if i % 2 != 0)

    print(score_t - score_a)


if __name__ == '__main__':
    resolve()
