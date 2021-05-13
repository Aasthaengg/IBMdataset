def q2():
    """ B - Golden Apple """
    N, D = (int(i) for i in input().split())
    d, m = divmod(N, D*2+1)
    if m > 0:
        d += 1
    print(d)


if __name__ == '__main__':
    q2()
