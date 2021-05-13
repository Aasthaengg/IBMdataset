

def read_input():
    a, b = map(int, input().split())
    return a, b


def submit():
    a, b = read_input()

    print(max(a - b, a + b, a * b))

if __name__ == '__main__':
    submit()
