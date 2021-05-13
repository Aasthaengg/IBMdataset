
def read_input():
    n = int(input())
    a = int(input())
    return n, a


def submit():
    n, a = read_input()
    print(n*n - a)


if __name__ == '__main__':
    submit()