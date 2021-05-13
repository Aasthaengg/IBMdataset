
def read_input():
    n, a, b = map(int, input().split())
    return n, a, b


def submit():
    n, a, b = read_input()
    print(min(b, n*a))


if __name__ == '__main__':
    submit()