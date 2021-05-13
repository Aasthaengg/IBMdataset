

def read_input():
    n, a, b = map(int, input().split())
    xlist = list(map(int, input().split()))
    return n, a, b, xlist


def submit():
    n, a, b, xlist = read_input()

    tired = 0

    for xs, xe in zip(xlist, xlist[1:]):
        dist = xe - xs

        if dist*a < b:
            tired += dist*a
        else:
            tired += b

    print(tired)
    return


if __name__ == '__main__':
    submit()
