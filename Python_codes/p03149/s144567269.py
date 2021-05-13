'''A - Beginning
https://atcoder.jp/contests/keyence2019/tasks/keyence2019_a

>>> main([1,7,9,4])
YES
>>> main([1,9,7,4])
YES
>>> main([1,2,9,1])
NO
>>> main([4,9,0,8])
NO
'''


def main(n):
    n = sorted(n)

    if n == [1, 4, 7, 9]:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    n = map(int, input().split(' '))
    main(n)
