def q1():
    a, b = (int(i) for i in input().split())
    ans = a * b
    if ans % 2 == 0:
        return 'Even'
    else:
        return 'Odd'


if __name__ == '__main__':
    print(q1())
