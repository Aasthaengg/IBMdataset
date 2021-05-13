def q2():
    r,D,x = (int(i) for i in input().split())
    for i in range(10):
        x = r * x - D
        print(x)


if __name__ == '__main__':
    q2()