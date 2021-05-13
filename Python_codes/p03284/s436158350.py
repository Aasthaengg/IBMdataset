'''A - AtCoder Crackers
https://atcoder.jp/contests/abc105/tasks/abc105_a

>>> main(7, 3)
1
>>> main(100, 10)
0
>>> main(1, 1)
0

>> main(78, 25)
1'''


def main(n, k):
    if n % k != 0:
        print(1)
    else:
        print(0)


if __name__ == "__main__":
    n, k = map(int, input().split(' '))
    main(n, k)
