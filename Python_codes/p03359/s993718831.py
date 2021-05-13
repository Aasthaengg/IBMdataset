
def read_input():
    a, b = map(int, input().split())
    return a, b


def submit():
    a, b = read_input()

    if a <= b:
        print(a)
    else:
        print(a - 1)

if __name__ == '__main__':
    submit()
