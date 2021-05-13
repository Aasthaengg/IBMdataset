import sys
from operator import itemgetter
input = sys.stdin.readline


def main():
    N = int(input())
    AB = [None] * N
    for i in range(N):
        A, B = map(int, input().split())
        AB[i] = (A, B, A + B)

    AB.sort(reverse=True, key=itemgetter(2))
    sum_A = 0
    sum_B = 0
    for i in range(N):
        if i % 2 == 0:
            sum_A += AB[i][0]
        else:
            sum_B += AB[i][1]

    ans = sum_A - sum_B
    print(ans)


if __name__ == "__main__":
    main()
