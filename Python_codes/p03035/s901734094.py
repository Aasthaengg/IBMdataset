def q1():
    A, B = (int(i) for i in input().split())
    if A >= 13:
        print(B)
    elif A >= 6:
        print(int(B / 2))
    else:
        print(0)


if __name__ == '__main__':
    q1()