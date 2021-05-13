

def read_input():
    a, b, c  = map(int, input().split())
    return a, b, c


def submit():
    a, b, c = read_input()

    if a + b < c:
        print('No')
    else:
        print('Yes')


if __name__ == '__main__':
    submit()
