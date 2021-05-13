
def read_input():
    a, b, c = map(int, input().split())
    return a, b, c


def submit():
    a, b, c = read_input()

    if b - a == c - b:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    submit()
